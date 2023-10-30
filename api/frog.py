from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import requests
import random

app = Flask(__name__)

# Frog species data
frog_species_data = [
    {
        "name": "Sumaco Horned Frog (Hemiphractus proboscideus)",
        "description": "The Sumaco Horned Frog is medium-sized, typically reaching a size of around 1.5 to 2 inches (3.8 to 5 centimeters).",
        "habitat": "The Sumaco Horned Frog is native to the cloud forests of Ecuador in South America. It is found in the Sumaco Volcano area, which is its namesake.",
        "predators": "Predators of the Sumaco Horned Frog may include snakes and certain birds that inhabit the same region.",
        "diet": "Sumaco Horned Frogs primarily feed on insects and small invertebrates in their natural habitat.",
        "lifespan": "The typical lifespan of the Sumaco Horned Frog in the wild is around 8 to 10 years.",
        "toxicity": "The Sumaco Horned Frog is not considered highly poisonous or toxic. It does not possess the potent skin toxins seen in some other frog species.",
        "interesting_facts": "The Sumaco Horned Frog gets its name from the distinctive bony horn-like protrusions above its eyes, which give it a unique appearance...",
    },
    {
        "name": "Peruvian Toad (Rhinella peruviana)",
        "description": "Peruvian Toads are medium to large-sized amphibians, typically reaching a size of around 2.4 to 4 inches (6 to 10 centimeters) in length.",
        "habitat": "Peruvian Toads are found in various countries in South America, including Peru, Ecuador, and Bolivia. They inhabit a range of environments, including tropical rainforests and montane forests...",
        "predators": "Predators of the Peruvian Toad may include snakes, large birds, and some mammals. They may also face threats from human activities, such as habitat destruction...",
        "diet": "Peruvian Toads are primarily insectivorous, and they feed on a diet consisting of a variety of insects and other invertebrates...",
        "lifespan": "The average lifespan of the Peruvian Toad in the wild is not precisely documented but is estimated to be around 5 to 10 years...",
        "toxicity": "The Peruvian Toad is a species known for its warty skin and distinctive coloration...",
        "interesting_facts": "The Peruvian Toad is part of the unique and diverse amphibian fauna of South America, and it contributes to the ecosystem by controlling insect populations...",
    },
    {
        "name": "Painted Burrowing Frog (Neobatrachus sudellae)",
        "description": "The Painted Burrowing Frog is a small-sized frog, typically ranging from about 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length...",
        "habitat": "The Painted Burrowing Frog is native to the southwestern regions of Western Australia. It is adapted to semi-arid and arid environments and can be found in sandy soils and heathland...",
        "predators": "Predators of the Painted Burrowing Frog can include snakes, birds, larger amphibians, and various reptiles that share its habitat...",
        "diet": "Painted Burrowing Frogs primarily feed on small invertebrates, including insects and other arthropods. They are known to eat ants, beetles, and other similar prey...",
        "lifespan": "The lifespan of the Painted Burrowing Frog in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more...",
        "toxicity": "The Painted Burrowing Frog is not known to be poisonous or toxic. It lacks the skin toxins found in some other frog species...",
        "interesting_facts": "The Painted Burrowing Frog gets its name from its distinctive marbled or painted appearance on its skin...",
    },
    {
        "name": "Lao Newt (Tylototriton lauhachindai)",
        "description": "The Lao Newt is a relatively small amphibian, typically measuring about 5 to 6 inches (12.5 to 15 centimeters) in length...",
        "habitat": "The Lao Newt is native to Laos and is primarily found in the mountainous regions of northern and central Laos. They inhabit cool, clear, and fast-flowing streams and small rivers...",
        "predators": "Predators of the Lao Newt may include various aquatic and semi-aquatic predators, such as larger fish, snakes, and some bird species...",
        "diet": "Lao Newts are carnivorous and primarily feed on aquatic invertebrates, such as small crustaceans, insects, and other small prey that they can capture in their aquatic habitat...",
        "lifespan": "The lifespan of the Lao Newt in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more...",
        "toxicity": "The Lao Newt is known to be toxic. Like other newt species, it possesses skin toxins that can be harmful to potential predators...",
        "interesting_facts": "The Lao Newt is part of the salamander family and is known for its distinctive coloration, with bright orange-red markings...",
    },
    {
        "name": "Eastern Spadefoot Toad (Scaphiopus holbrookii)",
        "description": "The Eastern Spadefoot Toad is a relatively small amphibian, typically ranging from 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length...",
        "habitat": "The Eastern Spadefoot Toad is native to the eastern and southeastern regions of the United States, where it can be found in sandy or loamy soils, including pine forests, grasslands, and scrub habitats...",
        "predators": "Predators of the Eastern Spadefoot Toad can include various snakes, birds, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates...",
        "diet": "Eastern Spadefoot Toads are insectivorous, primarily feeding on a diet of insects and other arthropods...",
        "lifespan": "The typical lifespan of Plains Leopard Frogs in the wild is around 2 to 4 years, although this can vary based on environmental conditions and predation...",
        "toxicity": "Eastern Spadefoot Toads are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species...",
        "interesting_facts": "These frogs get their name from the spots and blotchy patterns on their skin, resembling a leopard's spots...",
    },
    {
        "name": "Painted Reed Frog (Hyperolius marmoratus)",
        "description": "The Painted Reed Frog is a small-sized frog, typically ranging from about 0.8 to 1.2 inches (2 to 3 centimeters) in length...",
        "habitat": "The Painted Reed Frog is native to sub-Saharan Africa and is found in various countries across the continent...",
        "predators": "Predators of the Painted Reed Frog may include various birds, snakes, small mammals, and other amphibians...",
        "diet": "Painted Reed Frogs are insectivorous and primarily feed on a diet of small insects and invertebrates...",
        "lifespan": "The average lifespan of the Painted Reed Frog in the wild is not extensively documented but is estimated to be several years...",
        "toxicity": "The Painted Reed Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species...",
        "interesting_facts": "The Painted Reed Frog is known for its striking and colorful markings, which can vary in pattern and coloration...",
    },
    {
        "name": "Malagasy Rainbow Frog (Scaphiophryne gottlebei)",
        "description": "The Malagasy Rainbow Frog is a small to medium-sized frog, typically ranging from about 1.2 to 1.8 inches (3 to 4.5 centimeters) in length...",
        "habitat": "The Malagasy Rainbow Frog is native to Madagascar, an island nation off the southeastern coast of Africa...",
        "predators": "Predators of the Malagasy Rainbow Frog can include various snakes, birds, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates...",
        "diet": "Malagasy Rainbow Frogs are insectivorous and primarily feed on a diet of insects and other invertebrates...",
        "lifespan": "The average lifespan of the Malagasy Rainbow Frog in the wild is not extensively documented but is estimated to be several years...",
        "toxicity": "The Malagasy Rainbow Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species...",
        "interesting_facts": "The Malagasy Rainbow Frog is named for its striking and colorful patterns, which can vary among individuals...",
    },
    {
        "name": "Hourglass Tree Frog (Dendropsophus ebraccatus)",
        "description": "The Hourglass Tree Frog is a small-sized frog, typically ranging from about 1 to 1.5 inches (2.5 to 3.8 centimeters) in length...",
        "habitat": "This species is commonly found in the tropical rainforests of Central America and northern South America...",
        "predators": "Predators of the Hourglass Tree Frog can include snakes, birds, larger amphibians, and various small mammals. They may also be preyed upon by certain invertebrates...",
        "diet": "Hourglass Tree Frogs primarily feed on a diet of small insects and invertebrates, including ants, flies, and other arthropods...",
        "lifespan": "The average lifespan of the Hourglass Tree Frog
