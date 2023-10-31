import random

frogs_data = []

frog_list = [
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
        "lifespan": "The average lifespan of the Hourglass Tree Frog is around 5 years."
    }
     {
        "name": "Sumaco Horned Frog (Hemiphractus proboscideus)",
        "description": "The Sumaco Horned Frog is medium-sized, typically reaching a size of around 1.5 to 2 inches (3.8 to 5 centimeters).",
        "habitat": "The Sumaco Horned Frog is native to the cloud forests of Ecuador in South America. It is found in the Sumaco Volcano area, which is its namesake.",
        "predators": "Predators of the Sumaco Horned Frog may include snakes and certain birds that inhabit the same region.",
        "diet": "Sumaco Horned Frogs primarily feed on insects and small invertebrates in their natural habitat.",
        "lifespan": "The typical lifespan of the Sumaco Horned Frog in the wild is around 8 to 10 years.",
        "toxicity": "The Sumaco Horned Frog is not considered highly poisonous or toxic. It does not possess the potent skin toxins seen in some other frog species.",
        "interesting_facts": "The Sumaco Horned Frog gets its name from the distinctive bony horn-like protrusions above its eyes, which give it a unique appearance. These frogs have a cryptic coloration, often resembling moss or lichen, helping them blend into their forest environment. They are known for their unique reproductive behavior, with males guarding eggs and tadpoles, which they carry on their backs. This species is native to a specific and limited geographic range, making it an interesting subject of study and conservation concern."
    },
    {
        "name": "Peruvian Toad (Rhinella peruviana)",
        "description": "Peruvian Toads are medium to large-sized amphibians, typically reaching a size of around 2.4 to 4 inches (6 to 10 centimeters) in length.",
        "habitat": "Peruvian Toads are found in various countries in South America, including Peru, Ecuador, and Bolivia. They inhabit a range of environments, including tropical rainforests and montane forests.",
        "predators": "Predators of the Peruvian Toad may include snakes, large birds, and some mammals. They may also face threats from human activities, such as habitat destruction.",
        "diet": "Peruvian Toads are primarily insectivorous, and they feed on a diet consisting of a variety of insects and other invertebrates. Their diet may include ants, beetles, and other small arthropods.",
        "lifespan": "The average lifespan of the Peruvian Toad in the wild is not precisely documented but is estimated to be around 5 to 10 years.",
        "toxicity": "Peruvian Toads, like many toad species, secrete toxins through their skin, which can act as a defense against predators. However, these toxins can vary among individuals and may not be as potent as those of some other toad species.",
        "interesting_facts": "Peruvian Toads are adapted to a life in the trees and are often found perched on branches and leaves. They have a distinctive appearance and are known for their unique vocalizations during the breeding season."
    },
    {
        "name": "Painted Burrowing Frog (Neobatrachus sudellae)",
        "description": "The Painted Burrowing Frog is a small-sized frog, typically ranging from about 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length.",
        "habitat": "The Painted Burrowing Frog is native to the southwestern regions of Western Australia. It is adapted to semi-arid and arid environments and can be found in sandy soils and heathland.",
        "predators": "Predators of the Painted Burrowing Frog can include snakes, birds, larger amphibians, and various reptiles that share its habitat.",
        "diet": "Painted Burrowing Frogs primarily feed on small invertebrates, including insects and other arthropods. They are known to eat ants, beetles, and other similar prey.",
        "lifespan": "The lifespan of the Painted Burrowing Frog in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more.",
        "toxicity": "The Painted Burrowing Frog is not known to be poisonous or toxic. It lacks the skin toxins found in some other frog species.",
        "interesting_facts": "The Painted Burrowing Frog gets its name from its distinctive marbled or painted appearance on its skin."
    },
    {
        "name": "Plains Leopard Frog (Lithobates blairi)",
        "description": "Plains Leopard Frogs are medium-sized frogs, typically ranging from about 2 to 3 inches (5 to 7.6 centimeters) in length.",
        "habitat": "These frogs are found in a variety of habitats, including grasslands, prairies, wetlands, and semi-aquatic environments. They are native to parts of North America, including the Great Plains region.",
        "predators": "Predators of Plains Leopard Frogs may include snakes, birds, larger amphibians, and various small mammals. Additionally, they may face threats from certain invertebrates.",
        "diet": "Plains Leopard Frogs are insectivorous and primarily feed on a diet of insects, spiders, and other small invertebrates.",
        "lifespan": "The typical lifespan of Plains Leopard Frogs in the wild is around 2 to 4 years, although this can vary based on environmental conditions and predation.",
        "toxicity": "Plains Leopard Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
        "interesting_facts": "These frogs get their name from the spots and blotchy patterns on their skin, resembling a leopard's spots. They are known for their distinctive vocalizations during the breeding season, which sound like chuckling laughter. Plains Leopard Frogs are adapted to a variety of terrestrial and aquatic habitats, and they often inhabit grasslands and wetlands with temporary or semi-permanent water bodies. During the breeding season, males call from the water to attract females for mating."
    },
    {
        "name": "Coorg Yellow Bush Frog (Raorchestes luteolus)",
        "description": "Coorg Yellow Bush Frogs are relatively small frogs, typically measuring about 1.2 to 1.6 inches (3 to 4 centimeters) in length.",
        "habitat": "These frogs are native to the Western Ghats region of India, particularly in the Coorg region. They inhabit dense vegetation, including bushes and shrubs, in forested and hilly areas.",
        "predators": "Predators of Coorg Yellow Bush Frogs may include snakes, larger insects, and various birds.",
        "diet": "Coorg Yellow Bush Frogs primarily feed on small insects and arthropods that they can find in their natural habitat.",
        "lifespan": "The average lifespan of Coorg Yellow Bush Frogs in the wild is not extensively documented but is estimated to be several years.",
        "toxicity": "Coorg Yellow Bush Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
        "interesting_facts": "These frogs have a bright yellow coloration, which helps them blend into the vegetation of their habitat. Coorg Yellow Bush Frogs are known for their distinctive calls, which are often heard during the breeding season. These calls help them communicate and locate potential mates. They are adapted to an arboreal (tree-dwelling) lifestyle and are often found perched on leaves and branches. The species is native to a region with rich biodiversity, and it contributes to the local ecosystem by controlling insect populations."
    },
    {
        "name": "Starry Night Reed Frog (Hyperolius pusillus)",
        "description": "Starry Night Reed Frogs are small-sized frogs, typically ranging from about 0.8 to 1.2 inches (2 to 3 centimeters) in length.",
        "habitat": "These frogs are native to sub-Saharan Africa and are found in various countries across the continent. They inhabit a range of environments, including savannas, grasslands, and reed beds near freshwater sources.",
        "predators": "Predators of Starry Night Reed Frogs may include various birds, snakes, small mammals, and other amphibians. They are vulnerable to a variety of animals that share their habitat.",
        "diet": "Starry Night Reed Frogs are insectivorous and primarily feed on a diet of small insects and invertebrates. They are known to consume prey such as small flies and other arthropods.",
        "lifespan": "The average lifespan of Starry Night Reed Frogs in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
        "toxicity": "Starry Night Reed Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
        "interesting_facts": "The Starry Night Reed Frog is known for its striking and colorful markings, which can vary in pattern and coloration. These patterns are often used for camouflage in their reed bed habitats. They have a unique breeding behavior, with males calling from the vegetation near water to attract females for mating. Starry Night Reed Frogs are well adapted to their freshwater environments and are excellent climbers, often found clinging to vegetation near water. These frogs are relatively small and have a charming, colorful appearance, making them a popular subject for amphibian enthusiasts and photographers."
    },
    {
        "name": "Yellow-striped Poison Dart Frog (Dendrobates truncatus)",
        "description": "Yellow-striped Poison Dart Frogs are typically small, with an average length of about 1 to 1.5 inches (2.5 to 4 centimeters).",
        "habitat": "They are primarily found in the tropical rainforests of South America, particularly in countries like Brazil and Peru. These frogs are often associated with lowland rainforests and can be found near small streams, ponds, and other water sources.",
        "predators": "While they are small and brightly colored, these frogs are highly toxic, which serves as a defense mechanism against predators. However, certain snake species and some birds have developed a resistance to their toxins and may prey on them.",
        "diet": "Yellow-striped Poison Dart Frogs primarily feed on small arthropods, including ants, termites, mites, and other small invertebrates. Their diet plays a crucial role in the development of their toxic skin secretions.",
        "lifespan": "In the wild, their lifespan is not extensively documented, but it is estimated to be several years. In captivity, with proper care, they can live for more extended periods.",
        "toxicity": "These frogs are indeed poisonous. They get their name from the toxic secretions on their skin, which can be harmful or even deadly to potential predators. Indigenous people have used the toxins from these frogs to poison the tips of blowdarts for hunting.",
        "interesting_facts": "These frogs are known for their bright and striking coloration, which can vary among individuals. The vibrant colors act as a warning signal to potential predators. Indigenous people of South America have used the toxins from these frogs for centuries to poison their blowdarts, which is why they are called 'dart frogs.' Their toxicity is believed to be a result of their diet, as they obtain certain alkaloids from the arthropods they consume."
    }
     {
        "name": "Archey's Frog (Leiopelma archeyi)",
        "description": "Archey's Frogs are small amphibians, with adults measuring about 3 to 4.4 centimeters (1.2 to 1.7 inches) in length. They have a compact and robust body structure.",
        "habitat": "These frogs are endemic to New Zealand and are found on the North Island. They inhabit cool, moist, and dense forest environments, often near streams and wetlands. They are particularly associated with areas of high rainfall.",
        "predators": "While adult Archey's Frogs have few natural predators, invasive species like rats, stoats, and other introduced mammals pose a significant threat to their eggs and tadpoles. Invasive species have led to a decline in their population.",
        "diet": "Archey's Frogs are primarily insectivorous, with a diet consisting of small invertebrates like insects, spiders, and other arthropods. They are known for their slow feeding behavior.",
        "lifespan": "In the wild, their lifespan can extend up to 30 years, making them one of the longest-lived frogs known. This longevity is remarkable for a small amphibian.",
        "toxicity": "Archey's Frogs are not known to be poisonous or toxic. They lack the potent skin toxins found in some other frog species. Instead, their main defense strategy is their cryptic appearance and living in remote, hard-to-reach habitats.",
        "interesting_facts": "These frogs have a limited range and are often considered 'living fossils' because they have changed very little over millions of years of evolution. They belong to an ancient lineage of frogs. They are often referred to as 'pepeketua' in the Māori language, which translates to 'the night creeper,' referencing their nocturnal habits. Archey's Frogs have a distinctive appearance, with rough, granular skin that helps with camouflage in their forested habitat."
    },
    {
        "name": "Red-legged Frog (Rana aurora)",
        "description": "Red-legged Frogs are considered relatively large for a frog species, with adults typically reaching sizes of 5.5 to 11 centimeters (2.2 to 4.3 inches) in length.",
        "habitat": "They are found in a variety of habitats, including freshwater bodies like ponds, lakes, marshes, and slow-moving streams. They are also known to inhabit terrestrial environments near aquatic habitats. Red-legged Frogs are primarily found in the western United States and southwestern Canada.",
        "predators": "The Red-legged Frog faces predation from a variety of animals, including birds, mammals, snakes, larger amphibians, and some invertebrates like insects. Introduced fish species can also be a threat to their eggs and tadpoles.",
        "diet": "Red-legged Frogs are carnivorous and primarily feed on a diet of insects, small invertebrates, and even smaller vertebrates. Their diet may include various insects, spiders, worms, and other small prey items found in their aquatic and terrestrial habitats.",
        "lifespan": "In the wild, Red-legged Frogs can have a lifespan of up to 8 years or more. Their longevity can vary depending on environmental conditions, predation, and other factors.",
        "toxicity": "While they are not as poisonous as some other frog species, Red-legged Frogs do secrete mild toxins through their skin, which can make them unpalatable to some predators. However, their level of toxicity is not as potent as, for example, poison dart frogs.",
        "interesting_facts": "Red-legged Frogs are often recognized by their distinct red coloration on the undersides of their hind legs, which gives them their name. They are excellent jumpers and swimmers, capable of leaping great distances and navigating through aquatic environments. Red-legged Frogs are known for their distinct, resonant call, which is often described as sounding like 'jug-o-rum'. They are considered an ecologically important species, playing a role in regulating insect populations and serving as prey for various predators in their habitat."
    },
    {
        "name": "European Common Frog (Rana temporaria)",
        "description": "European Common Frogs are relatively small to medium-sized frogs, with adults typically ranging from 6 to 9 centimeters (2.4 to 3.5 inches) in length.",
        "habitat": "These frogs are widespread across Europe and can be found in a variety of habitats, including woodlands, grasslands, wetlands, gardens, and urban areas. They are known for their adaptability to different environments.",
        "predators": "Predators of the European Common Frog can include a range of animals such as birds, snakes, larger amphibians, and some mammals. They may also face threats from various invertebrates. These frogs are an important food source for many animals in their ecosystems.",
        "diet": "European Common Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates. Their diet may include ants, flies, beetles, and other similar prey items.",
        "lifespan": "In the wild, European Common Frogs typically have a lifespan of about 4 to 8 years, although their longevity can vary based on environmental conditions and threats.",
        "toxicity": "European Common Frogs are not considered highly poisonous or toxic. They do not possess the potent skin toxins seen in some other frog species. However, they can secrete mild toxins, making them less palatable to predators.",
        "interesting_facts": "European Common Frogs are known for their unique call, which is often heard during the breeding season. The males produce a sound similar to a soft 'ribbit' to attract females. They have a wide range of color variations, including brown, green, and even reddish tones, depending on their surroundings and environmental conditions. During the winter, these frogs hibernate in protected sites, such as leaf litter and underground burrows, to survive the cold temperatures."
    },
    {
        "name": "Oriental Fire-bellied Toad (Bombina orientalis)",
        "description": "Oriental Fire-bellied Toads are relatively small in size, typically ranging from 3.2 to 5.5 centimeters (1.3 to 2.2 inches) in length.",
        "habitat": "These toads are native to a wide range of habitats, including various regions in Asia. They are commonly found in wetland areas, such as ponds, marshes, and slow-moving streams. They are well adapted to both terrestrial and aquatic environments.",
        "predators": "Predators of the Oriental Fire-bellied Toad may include snakes, birds, larger amphibians, and some mammals. These toads have developed a unique defense mechanism. When threatened, they arch their bodies and display their brightly colored bellies as a warning signal to potential predators.",
        "diet": "Oriental Fire-bellied Toads are primarily insectivorous and feed on a diet of small invertebrates. They consume a variety of prey, including insects, spiders, and other small arthropods.",
        "lifespan": "In the wild, Oriental Fire-bellied Toads can live for an average of 5 to 10 years, although this can vary based on environmental conditions and predation.",
        "toxicity": "These toads are mildly toxic. They have skin glands that secrete toxins, which are not usually deadly but can be irritating to potential predators or even humans if the toads are handled. However, their bright coloration serves as a warning to deter predators.",
        "interesting_facts": "Oriental Fire-bellied Toads are known for their vibrant green and black coloration on their dorsal side and bright orange or red markings on their ventral side. This coloration serves as aposematism, a warning signal to potential predators. When threatened, these toads may secrete a milky substance from their skin that contains toxins, serving as a defense mechanism. They are semi-aquatic and have webbed feet, which are well-suited for swimming and hopping in and around water bodies. Oriental Fire-bellied Toads are often kept as pets due to their striking appearance and relatively simple care requirements in a captive environment."
    },
    {
        "name": "Brazilian Horned Frog (Ceratophrys aurita)",
        "description": "Brazilian Horned Frogs are relatively large, with adults typically ranging from 10 to 15 centimeters (4 to 6 inches) in length, although some individuals can grow even larger.",
        "habitat": "They are native to South America, primarily found in countries like Brazil and Uruguay. Brazilian Horned Frogs inhabit a range of environments, including tropical rainforests and wetlands. They are known to burrow in the ground, where they spend much of their time.",
        "predators": "Predators of Brazilian Horned Frogs may include birds, larger amphibians, snakes, and mammals. These frogs have a unique defense mechanism, using their wide mouth and powerful jaws to ambush and consume potential threats, including small vertebrates.",
        "diet": "Brazilian Horned Frogs are carnivorous and known for their voracious appetites. They primarily feed on insects, small vertebrates, and other prey that they can capture, thanks to their large mouth and quick strikes.",
        "lifespan": "In the wild, Brazilian Horned Frogs can live for an average of 5 to 10 years, although their lifespan may vary based on environmental conditions and the availability of food.",
        "toxicity": "Brazilian Horned Frogs are not considered highly poisonous or toxic in the same way some other frog species are. They do not possess potent skin toxins.",
        "interesting_facts": "Brazilian Horned Frogs get their name from the pointed, horn-like structures above their eyes, which give them a distinctive appearance. They are often referred to as 'Pacman frogs' due to their large mouth and round body shape. These frogs are sit-and-wait predators. They remain hidden in the leaf litter or soil, waiting for prey to come close, and then they strike with remarkable speed to capture their meal. Brazilian Horned Frogs are known for their adaptability to various environments and can be found in both pristine and disturbed habitats."
    },
    {
        "name": "Amazon Milk Frog (Trachycephalus resinifictrix)",
        "description": "Amazon Milk Frogs are medium-sized frogs, typically ranging from about 2 to 3 inches (5 to 7.5 centimeters) in length.",
        "habitat": "They are native to South America and can be found in countries like Brazil, Peru, and Colombia. Amazon Milk Frogs inhabit various environments, including rainforests, tropical lowlands, and wetlands. They are often found near freshwater sources.",
        "predators": "Predators of the Amazon Milk Frog may include various birds, snakes, and other amphibians. They may also face threats from larger insects and invertebrates. Their bright coloration is a warning signal to potential predators.",
        "diet": "Amazon Milk Frogs are insectivorous and primarily feed on a diet of insects and small invertebrates. They consume prey such as small flies, crickets, moths, and other arthropods.",
        "lifespan": "In the wild, Amazon Milk Frogs can live for up to 10 years or more, depending on environmental conditions and predation. Their lifespan can be influenced by factors such as habitat quality and availability of food.",
        "toxicity": "Amazon Milk Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species. However, they have a unique defense mechanism: when threatened, they excrete a milky secretion from their skin, which is a defensive strategy to deter predators.",
        "interesting_facts": "Amazon Milk Frogs are known for their vibrant green coloration, which serves as camouflage in their leafy habitats. Their bellies are typically creamy white. When threatened, they excrete a sticky, milky substance from their skin, giving them their common name 'Milk Frog.' These frogs are arboreal, meaning they spend a significant amount of time in trees and vegetation. Amazon Milk Frogs are skilled climbers, often found clinging to leaves and branches near water sources."
    },
    {
        "name": "Bumblebee Poison Dart Frog (Dendrobates leucomelas)",
        "description": "The Bumblebee Poison Dart Frog is a small frog, typically ranging from about 1 to 2 inches (2.5 to 5 centimeters) in length.",
        "habitat": "These frogs are native to South America and are found in countries like Venezuela, Colombia, and Brazil. They inhabit tropical rainforests and dense vegetation near freshwater sources like streams and small rivers.",
        "predators": "Despite their small size, Bumblebee Poison Dart Frogs have very few natural predators. This is because they are highly toxic. Their bright colors serve as a warning to potential predators. Only a few species in their habitat have developed immunity to their toxins.",
        "diet": "These frogs are insectivorous and primarily feed on a diet of small arthropods and insects. Their diet may include ants, termites, small beetles, and other tiny invertebrates.",
        "lifespan": "In the wild, Bumblebee Poison Dart Frogs have a relatively long lifespan for a frog, typically living up to 5-7 years or more. In captivity, where they are not exposed to natural predators and stressors, they can live even longer.",
        "toxicity": "Bumblebee Poison Dart Frogs are among the most toxic animals on Earth. They secrete potent neurotoxins through their skin, which can be deadly to potential predators. Indigenous people, such as the native tribes of South America, have been known to use the toxins from these frogs to poison the tips of blowdarts for hunting. However, in captivity, when they are not exposed to the same insects they would consume in the wild, they do not develop these toxins.",
        "interesting_facts": "Bumblebee Poison Dart Frogs are named for their distinctive black and yellow coloration, which resembles the colors of a bumblebee. This bold coloration serves as a warning to potential predators about their toxicity. The toxic compounds they secrete are known as batrachotoxins, and they are among the most potent natural toxins. Female Bumblebee Poison Dart Frogs lay their eggs in leaf litter on the forest floor. Once hatched, the female transports her tadpoles to small water-filled cavities in plants. These frogs are known for their intricate courtship rituals, which often involve calling and various body movements."
    },
    {
        "name": "Green and Black Poison Dart Frog (Dendrobates auratus)",
        "description": "The Green and Black Poison Dart Frog is a small-sized frog, typically ranging from 3 to 5 centimeters (1.2 to 2 inches) in length.",
        "habitat": "They are native to Central and South America, particularly in tropical rainforests, moist lowland forests, and near streams and rivers.",
        "predators": "Natural predators of the Green and Black Poison Dart Frog include various birds, snakes, larger amphibians, and certain mammals.",
        "diet": "They are insectivores and primarily feed on a variety of small invertebrates, including ants, beetles, and other insects.",
        "lifespan": "In the wild, they can live for about 3 to 6 years. In captivity with proper care, they may live up to 10 years or more.",
        "toxicity": "The Green and Black Poison Dart Frog is highly toxic. They possess potent skin toxins, particularly batrachotoxin, which is one of the most toxic substances known to humans.",
        "interesting_facts": "The bright coloration of this frog serves as a warning to potential predators about their toxicity. Indigenous people have used the toxins from these frogs to coat the tips of blowdarts for hunting, giving them the name dart frogs. They are known for their complex social behaviors, including courtship rituals and territorial defense."
    },
    {
        "name": "Pine Barrens Treefrog (Hyla andersonii)",
        "description": "The Pine Barrens Treefrog is a small-sized frog, typically ranging from 2.5 to 5.5 centimeters (1 to 2.2 inches) in length.",
        "habitat": "They are primarily found in the United States, specifically in the Pine Barrens region of New Jersey. They inhabit wetlands, bogs, swamps, and forested areas with slow-moving water bodies.",
        "predators": "Natural predators of the Pine Barrens Treefrog include birds, snakes, larger amphibians, and various mammals.",
        "diet": "They are insectivores and primarily feed on a variety of insects, including flies, beetles, ants, and other small invertebrates.",
        "lifespan": "In the wild, Pine Barrens Treefrogs can live for about 3 to 7 years. However, their lifespan may vary depending on environmental factors.",
        "toxicity": "The Pine Barrens Treefrog is not known to be poisonous or toxic to humans.",
        "interesting_facts": "They are known for their distinctive call, which sounds like a series of honks or quacks, similar to the call of a duck. The Pine Barrens Treefrog is considered a species of special concern due to its limited range and habitat loss. Their coloration helps them blend in with their surroundings, making them well-adapted to their wetland habitats."
    }
    {
        "name": "Moor Frog (Rana arvalis)",
        "description": "The Moor Frog is a medium-sized frog, typically ranging from 6 to 9 centimeters (2.4 to 3.5 inches) in length.",
        "habitat": "Moor Frogs are primarily found in Europe, particularly in damp and boggy habitats. They inhabit a variety of wetland environments including marshes, peat bogs, and meadows with seasonal ponds.",
        "predators": "The main predators of Moor Frogs include birds (such as herons and gulls), snakes, larger amphibians, and mammals like foxes and martens.",
        "diet": "They are insectivores and primarily feed on a variety of insects and invertebrates found in their wetland habitats.",
        "lifespan": "In the wild, Moor Frogs typically live for about 4 to 8 years. However, their lifespan can vary depending on environmental conditions and predation.",
        "toxicity": "Moor Frogs are not considered poisonous or toxic to humans.",
        "interesting_facts": "Male Moor Frogs are known for their distinctive blue coloration during the breeding season. This blue coloration is temporary and is used to attract females. They are highly adapted to life in wetland habitats and have specialized webbed feet for efficient swimming. Moor Frogs are considered an important species for the health of wetland ecosystems as they help control insect populations."
    },
    {
        "name": "Western Chorus Frog (Pseudacris triseriata)",
        "description": "The Western Chorus Frog is a small-sized frog, typically ranging from 2.5 to 4 centimeters (1 to 1.6 inches) in length.",
        "habitat": "Western Chorus Frogs are native to North America and can be found in a wide range of habitats including grasslands, meadows, swamps, and forested areas. They are known for their adaptability to both wet and dry environments.",
        "predators": "Natural predators of the Western Chorus Frog include birds (such as herons and owls), snakes, larger amphibians, and various mammals.",
        "diet": "They are insectivores and primarily feed on a variety of insects and small invertebrates found in their habitat, including flies, ants, and beetles.",
        "lifespan": "In the wild, Western Chorus Frogs typically live for about 3 to 7 years.",
        "toxicity": "Western Chorus Frogs are not considered poisonous or toxic to humans.",
        "interesting_facts": "Western Chorus Frogs are known for their distinctive and repetitive calls, which resemble the sound of running a thumbnail along the teeth of a comb. This call is often described as sounding like crreeeek... crreeeek. They are highly adaptable and can thrive in a variety of habitats, making them one of the most widely distributed frogs in North America. These frogs are known for their color variation, which can range from green to brown, depending on factors like temperature and habitat."
    },
    {
        "name": "Burmese Peacock Frog (Pseudophilautus species)",
        "description": "The Burmese Peacock Frog is a small-sized frog, typically ranging from 2.5 to 3 centimeters (1 to 1.2 inches) in length.",
        "habitat": "The Burmese Peacock Frog is native to the forests of Myanmar (Burma). They are primarily found in tropical and subtropical rainforests, where they inhabit leaf litter and moist environments.",
        "predators": "Predators of the Burmese Peacock Frog may include birds, snakes, larger amphibians, and certain mammals.",
        "diet": "They are insectivores and primarily feed on a variety of small invertebrates, including ants, beetles, and other insects found in the leaf litter.",
        "lifespan": "The exact lifespan of the Burmese Peacock Frog in the wild may vary, but it is generally expected to be a few years.",
        "toxicity": "While specific toxicity information for all Pseudophilautus species may not be widely documented, some members of the genus are known to produce skin toxins as a defense mechanism. It is advisable to exercise caution when handling any wild frog, especially if its toxicity is unknown.",
        "interesting_facts": "The Burmese Peacock Frog gets its name from the vibrant and striking coloration of some species, resembling the colors of a peacock. Many species of the Pseudophilautus genus are known for their unique and melodious calls, which vary between different species."
    },
    {
        "name": "Parachute Frog (Rhacophorus species)",
        "description": "Parachute Frogs are typically medium-sized frogs, ranging from 4 to 7 centimeters (1.6 to 2.8 inches) in length.",
        "habitat": "Parachute Frogs are found in various parts of Asia, including countries like India, China, Malaysia, and Indonesia. They inhabit tropical rainforests, often in hilly or mountainous regions, where they are adapted to arboreal (tree-dwelling) lifestyles.",
        "predators": "The natural predators of Parachute Frogs include birds of prey, snakes, larger amphibians, and some mammals.",
        "diet": "They are insectivores and primarily feed on a variety of insects, including flies, ants, and other small invertebrates found in the forest canopy.",
        "lifespan": "Some species of Parachute Frogs are known to possess skin toxins as a defense mechanism. These toxins can be harmful to predators, and in some cases, even to humans. However, not all species within the genus Rhacophorus are toxic, and the level of toxicity may vary.",
        "interesting_facts": "Parachute Frogs are named for their unique ability to glide or parachute from tree to tree using specialized webbed feet and skin flaps (patagia) that allow them to catch air and glide. Mating behavior in some species involves the male creating a foam nest on leaves overhanging water. The female lays her eggs in this nest, and the male guards and tends to them until they hatch."
    },
    {
        "name": "Malaysian Horned Frog (Megophrys nasuta)",
        "description": "The Malaysian Horned Frog is a relatively large frog, with adults typically ranging from 8 to 14 centimeters (3 to 5.5 inches) in length.",
        "habitat": "These frogs are native to Southeast Asia, including countries like Malaysia, Thailand, Indonesia, and surrounding regions. They are often found in humid tropical rainforests, as well as in grasslands and wetlands.",
        "predators": "Predators of the Malaysian Horned Frog may include birds, snakes, larger amphibians, and some mammals.",
        "diet": "They are sit-and-wait predators, primarily feeding on a diet of insects and small invertebrates. They are known to consume a wide variety of prey items including insects, spiders, and even small vertebrates.",
        "lifespan": "While the Malaysian Horned Frog is not considered highly toxic, they do possess skin toxins as a defense mechanism. These toxins can cause mild irritation or discomfort if they come into contact with mucous membranes or open wounds.",
        "interesting_facts": "The distinctive horns on their heads are actually bony extensions, known as supraorbital dermal appendages. These structures help them blend into their surroundings by resembling leaf litter or small branches. When threatened, Malaysian Horned Frogs can inflate themselves, making them appear larger and potentially deterring predators."
    }
    {
        "name": "Mantella Frog (Mantella species)",
        "description": "Mantella Frogs are typically small-sized frogs, ranging from 2.5 to 5 centimeters (1 to 2 inches) in length.",
        "habitat": "Mantella Frogs are native to Madagascar, an island off the coast of Africa. They are primarily found in tropical rainforests, marshes, and moist lowland areas.",
        "predators": "Natural predators of Mantella Frogs include various birds, snakes, larger amphibians, and certain mammals.",
        "diet": "They are insectivores and primarily feed on a variety of insects and small invertebrates found in their habitats.",
        "lifespan": "In the wild, Mantella Frogs typically live for about 5 to 8 years. However, their lifespan can vary depending on environmental conditions.",
        "toxicity": "Many species of Mantella Frogs are known to be toxic or poisonous. They have bright and warning coloration, which serves as an indicator of their toxicity to potential predators.",
        "interesting_facts": "Mantella Frogs are known for their vibrant and striking colors, which can range from bright reds and oranges to blues and yellows. These colors serve as a warning to predators about their toxicity. They are often referred to as Madagascar's poison dart frogs due to their similarity in appearance and toxicity to the poison dart frogs found in Central and South America. Mantella Frogs have a unique and complex courtship behavior, which includes vocalizations and various visual displays."
    },
    {
        "name": "Greening Frog (Hyla gratiosa)",
        "description": "The Greening Frog, also known as the Barking Treefrog, is a medium-sized frog, typically ranging from 5 to 8 centimeters (2 to 3.1 inches) in length.",
        "habitat": "They are native to the southeastern United States, including parts of Florida, Georgia, South Carolina, and Alabama. They are typically found in wetland habitats like swamps, marshes, ponds, and slow-moving streams.",
        "predators": "Natural predators of the Greening Frog include birds, snakes, larger amphibians, and various mammals.",
        "diet": "They are insectivores and primarily feed on a variety of insects and small invertebrates found in their wetland habitats.",
        "lifespan": "In the wild, Greening Frogs typically live for about 3 to 5 years. However, their lifespan can vary depending on environmental conditions and predation.",
        "toxicity": "Greening Frogs are not considered poisonous or toxic to humans.",
        "interesting_facts": "The Greening Frog gets its name from the vocalization that sounds like a dog's bark or a goose's honk. This distinctive call is most commonly heard during the breeding season. They have adhesive toe pads that allow them to climb and cling to vegetation, making them well-adapted to their arboreal lifestyle."
    },
    {
        "name": "White's Tree Frog (Litoria caerulea)",
        "description": "White's Tree Frog is a medium to large-sized frog, typically ranging from 10 to 14 centimeters (4 to 5.5 inches) in length.",
        "habitat": "They are native to northern and eastern parts of Australia, but due to their popularity in the pet trade, they can now be found in various parts of the world. They inhabit a wide range of environments including tropical rainforests, savannas, and even urban areas.",
        "predators": "Natural predators of White's Tree Frog include various birds, snakes, and larger amphibians. Additionally, some mammals and large insects may also prey on them.",
        "diet": "They are insectivores and primarily feed on a variety of insects such as crickets, cockroaches, moths, and beetles.",
        "lifespan": "In captivity, White's Tree Frogs can live up to 16 years or more with proper care. In the wild, their lifespan is generally shorter due to various environmental factors.",
        "toxicity": "White's Tree Frog is not considered toxic or poisonous to humans.",
        "interesting_facts": "They are often referred to as dumpy tree frogs due to their plump appearance. White's Tree Frogs have a distinctive, loud, and sometimes shrill call that sounds like a honking horn. They have a unique adaptation that allows them to absorb moisture through their skin, which is particularly useful in arid environments."
    },
    {
        "name": "Vietnamese Mossy Frog (Theloderma corticale)",
        "description": "Vietnamese Mossy Frogs are relatively small, with adults typically measuring about 2 to 2.5 inches (5 to 6.5 centimeters) in length.",
        "habitat": "These frogs are native to northern Vietnam and are often found in montane cloud forests and hilly regions. They are well adapted to life in forested areas with dense vegetation, where they can hide among moss and foliage.",
        "predators": "While they are not well-documented, potential predators of Vietnamese Mossy Frogs may include snakes, larger amphibians, and some birds. These frogs are cryptic and well-camouflaged, which helps them avoid detection by predators.",
        "diet": "Vietnamese Mossy Frogs are insectivorous and primarily feed on a diet of small invertebrates, including insects and arachnids. They use their long, sticky tongues to capture prey.",
        "lifespan": "In the wild, their lifespan is not extensively documented, but it's estimated to be several years, possibly up to a decade or more, depending on environmental conditions and predation.",
        "toxicity": "Vietnamese Mossy Frogs are not known to be poisonous or toxic like some other frog species. They rely on their cryptic coloration and behavior rather than toxins for protection.",
        "interesting_facts": "The Vietnamese Mossy Frog gets its name from its unique appearance. Their skin is covered in tubercles and irregularly shaped protuberances, giving them a mossy or lichen-like appearance, which serves as camouflage in their forest habitat. These frogs have an unusual breeding behavior. The female lays her eggs in plant leaves overhanging water, and when the tadpoles hatch, they drop into the water below to continue their development. They are primarily arboreal, meaning they spend a significant portion of their lives in trees and shrubs."
    },
    {
        "name": "Coqui Frog (Eleutherodactylus coqui)",
        "description": "Coqui Frogs are relatively small, typically ranging from about 1 to 2 inches (2.5 to 5 centimeters) in length.",
        "habitat": "These frogs are native to Puerto Rico, but they have been introduced to other regions, including Hawaii and New Zealand. They are often found in a variety of habitats, including forests, grasslands, gardens, and urban areas. Coqui Frogs have adapted well to human-altered environments.",
        "predators": "In their native habitat, Coqui
        "predators": "In their native habitat, Coqui Frogs have several predators, including birds, snakes, and some insects. However, their invasive presence in regions like Hawaii has created ecological imbalances, as they lack natural predators in these areas.",
        "diet": "Coqui Frogs are insectivores and primarily feed on a diet of various small invertebrates, including insects such as ants, flies, and other arthropods.",
        "lifespan": "The lifespan of Coqui Frogs in the wild can vary, but they typically live for several years, with some individuals living up to five years.",
        "toxicity": "Coqui Frogs are not known to be poisonous or toxic. They rely on their ability to blend into their surroundings and their rapid reproductive rate as a survival strategy.",
        "interesting_facts": "Coqui Frogs are known for their distinctive 'co-qui' call, which is often used to locate other frogs and establish territory. This call can be quite loud and persistent, especially in areas where they have become invasive, causing noise disturbances to local residents. These frogs are known for their high reproductive rate, with females laying large clutches of eggs. Their adaptability to different habitats and rapid reproduction have contributed to their invasive success in some regions. In areas where Coqui Frogs have become invasive, they can have negative ecological impacts on local ecosystems. Their presence can disrupt native ecosystems and threaten native species."
    }
    {
    "Coqui Frog (Eleutherodactylus coqui)": 
        "description": "Coqui Frogs are relatively small, typically ranging from about 1 to 2 inches (2.5 to 5 centimeters) in length.",
        "habitat": "These frogs are native to Puerto Rico, but they have been introduced to other regions, including Hawaii and New Zealand. They are often found in a variety of habitats, including forests, grasslands, gardens, and urban areas. Coqui Frogs have adapted well to human-altered environments.",
        "predators": "In their native habitat, Coqui Frogs have several predators, including birds, snakes, and some insects. However, their invasive presence in regions like Hawaii has created ecological imbalances, as they lack natural predators in these areas.",
        "diet": "Coqui Frogs are insectivores and primarily feed on a diet of various small invertebrates, including insects such as ants, flies, and other arthropods.",
        "lifespan": "The lifespan of Coqui Frogs in the wild can vary, but they typically live for several years, with some individuals living up to five years.",
        "toxicity": "Coqui Frogs are not known to be poisonous or toxic. They rely on their ability to blend into their surroundings and their rapid reproductive rate as a survival strategy.",
        "interesting_facts": "Coqui Frogs are known for their distinctive 'co-qui' call, which is often used to locate other frogs and establish territory. This call can be quite loud and persistent, especially in areas where they have become invasive, causing noise disturbances to local residents. These frogs are known for their high reproductive rate, with females laying large clutches of eggs. Their adaptability to different habitats and rapid reproduction have contributed to their invasive success in some regions. In areas where Coqui Frogs have become invasive, they can have negative ecological impacts on local ecosystems. Their presence can disrupt native ecosystems and threaten native species."
    },
    "Budgett's Frog (Paraguay Frog, Paratelmatobius cf. poecilogaster)": 
        "description": "Budgett's Frogs are relatively large compared to many other frog species, typically reaching sizes of 3 to 4 inches (7.5 to 10 centimeters) in length. They have a distinctive appearance with a flattened body and a 'grinning' mouth, which gives them a distinctive and somewhat comical look.",
        "habitat": "These frogs are native to South America, specifically regions in Paraguay, Argentina, and Bolivia. They are often found in lowland areas, typically inhabiting marshes, ponds, and wetlands.",
        "predators": "Budgett's Frogs have several predators, including snakes, birds, and larger amphibians. Their unique appearance, with a wide mouth and somewhat intimidating appearance, might deter some predators.",
        "diet": "These frogs are known to feed on a diet consisting primarily of insects, particularly aquatic insects, small vertebrates, and other prey that they can find in their aquatic habitat.",
        "lifespan": "The precise lifespan of Budgett's Frogs in the wild is not extensively documented, but they can live for several years under suitable conditions, possibly up to a decade or more.",
        "toxicity": "Budgett's Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species, and their defense strategy primarily relies on their appearance.",
        "interesting_facts": "Budgett's Frogs are known for their distinctive appearance, which includes a wide, grinning mouth. This appearance is often referred to as a 'smiling frog' or 'Paraguay Horned Frog.' Their unique appearance, with a flattened body and mouth, helps them blend into their aquatic environment, making them excellent ambush predators. While not highly poisonous, their appearance might serve as a deterrent to potential predators."
    },
    "Solomon Island Leaf Frog (Ceratobatrachus guentheri)": {
        "description": "These frogs are relatively small, with adults typically ranging from about 1.2 to 2 inches (3 to 5 centimeters) in length.",
        "habitat": "The Solomon Island Leaf Frog is native to the Solomon Islands in the southwestern Pacific Ocean. They are primarily found in rainforests and are often associated with leaves and vegetation near small streams and other water bodies.",
        "predators": "While specific predators of the Solomon Island Leaf Frog aren't extensively documented, they may face threats from various rainforest-dwelling predators, such as snakes, birds, and larger amphibians.",
        "diet": "These frogs are insectivorous, primarily feeding on a diet consisting of small insects and invertebrates found in their rainforest habitat.",
        "lifespan": "The precise lifespan of the Solomon Island Leaf Frog in the wild isn't well-documented, but it is estimated to be several years, typically up to 5 years or more, depending on environmental conditions and predation.",
        "toxicity": "The Solomon Island Leaf Frog is not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
        "interesting_facts": "These frogs are known for their striking green coloration and unique leaf-like appearance, which helps them blend into their rainforest habitat. Their large, webbed feet and the fringed edges of their skin flaps aid in gliding from tree to tree, giving them a unique ability to move through the rainforest canopy. Solomon Island Leaf Frogs are adapted to an arboreal (tree-dwelling) lifestyle and are skilled climbers, often found in vegetation above water."
    },
    "Paraguay Horned Frog (Ceratophrys cranwelli)": {
        "description": "Paraguay Horned Frogs are relatively large amphibians. They can reach sizes of around 3 to 4.7 inches (7.5 to 12 centimeters) in length.",
        "habitat": "These frogs are native to parts of South America, including Paraguay and Argentina. They inhabit semi-aquatic environments, such as swamps, marshes, and slow-moving water bodies.",
        "predators": "Common predators of the Paraguay Horned Frog include various birds, snakes, and larger amphibians. These frogs are ambush predators, and they have a large mouth for capturing prey.",
        "diet": "Paraguay Horned Frogs are carnivorous and primarily feed on a diet of insects, small vertebrates, and other prey that they can capture using their impressive, gaping mouth. They are known to eat a variety of creatures, including other frogs, small rodents, and insects.",
        "lifespan": "In the wild, Paraguay Horned Frogs typically have a lifespan of up to 5 to 10 years, depending on environmental conditions and predation.",
        "toxicity": "While these frogs are not typically considered poisonous, they have a defense mechanism involving inflating their bodies when threatened, which can make them less palatable to potential predators. They also have strong jaws and sharp teeth, which can deliver a powerful bite if necessary.",
        "interesting_facts": "The Paraguay Horned Frog gets its name from the bony, horn-like projections over its eyes, which are believed to serve a defensive purpose. They have a broad mouth and a voracious appetite, often consuming prey nearly the same size as themselves. These frogs are known for their unique and powerful bite, and they are sometimes referred to as 'Pac-Man frogs' because of their mouth size and feeding behavior. Paraguay Horned Frogs are adapted to a semi-aquatic lifestyle and are often found near water. They spend much of their time lying in wait for unsuspecting prey."
    },
    "Fire-bellied Toad (Bombina species)": {
        "description": "Fire-bellied toads are relatively small, with adults typically ranging from 1.2 to 2.4 inches (3 to 6 centimeters) in length.",
        "habitat": "Fire-bellied toads are native to a broad range of habitats, primarily in Europe and Asia. They can be found in various environments, including forests, grasslands, marshes, and ponds. They are semi-aquatic and often inhabit areas with freshwater.",
        "predators": "Predators of Fire-bellied toads can include birds, snakes, larger amphibians, and some mammals. Due to their small size and vibrant coloration, these toads rely on their warning colors to deter potential predators.",
        "diet": "Fire-bellied toads are insectivorous and primarily feed on a diet of small invertebrates, such as insects and other arthropods. Their diet may include ants, beetles, and various small prey they can find in or near the water.",
        "lifespan": "In the wild, Fire-bellied toads typically have a lifespan of up to 10 to 15 years, depending on environmental conditions and predation.",
        "toxicity": "Fire-bellied toads are known for their colorful ventral (belly) skin, which typically features bright red or orange coloration. This serves as a warning to potential predators that they are toxic. They produce toxins through their skin glands, which can be irritating or even toxic to predators that attempt to consume them. While not extremely toxic to humans, it's essential to handle them with care.",
        "interesting_facts": "Fire-bellied toads are named for their strikingly colorful belly patterns, which they display as a warning signal to potential predators. These toads are well adapted to both terrestrial and aquatic environments, often found near water bodies. They are known for their unique behavior of arching their bodies and displaying their bright, contrasting colors when they feel threatened. Some species within the Bombina genus are popular as pets in the exotic pet trade, thanks to their vibrant coloration and relatively small size."
    }
{
    "Goliath Frog (Conraua goliath)": {
        "description": "The Goliath Frog is one of the largest frog species in the world. Adult Goliath Frogs can reach a length of up to 12.6 inches (32 centimeters) and weigh up to 3.3 kilograms (7.3 pounds). Tadpoles of this species can also grow to substantial sizes.",
        "habitat": "Goliath Frogs are native to the rainforests of Central and West Africa, specifically found in the regions of Equatorial Guinea and Cameroon. They inhabit fast-flowing rivers and streams within the dense rainforest, preferring areas with rocky substrates.",
        "predators": "Despite their impressive size, Goliath Frogs have some natural predators. Their primary predators include large water birds, such as herons, and various aquatic predators. Additionally, humans pose a threat due to habitat destruction and over-harvesting.",
        "diet": "Goliath Frogs are opportunistic carnivores, primarily feeding on a diet of insects, small vertebrates, and invertebrates that they can capture near the water's edge. They are known to consume a variety of prey, including insects, crabs, and small fish.",
        "lifespan": "The exact lifespan of Goliath Frogs in the wild is not well-documented, but they are believed to live several years. In captivity, they may live longer, potentially up to 15 years.",
        "toxicity": "Goliath Frogs are not known to be poisonous or toxic in the same way some other frog species are. They rely more on their size and camouflage for protection.",
        "interesting_facts": "Goliath Frogs are the world's largest frogs, both in terms of size and weight. Their massive appearance and size distinguish them from most other frog species. They have a remarkable and unique breeding behavior, where the male frogs call loudly to attract females. The female Goliath Frogs lay their eggs in or near fast-flowing rivers, and the male guards the eggs and tadpoles until they metamorphose into froglets. The large size of Goliath Frogs is thought to be an adaptation to the fast-flowing streams they inhabit. Their size helps them withstand the strong currents and maintain their position within the water. Goliath Frogs have a greenish-brown coloration with mottled patterns on their skin, which provides excellent camouflage in their lush rainforest environment."
    },
    "Wood Frog (Rana sylvatica)": {
        "description": "Wood Frogs are small to medium-sized amphibians, typically ranging from about 2 to 2.75 inches (5 to 7 centimeters) in length.",
        "habitat": "Wood Frogs are found in various parts of North America, primarily in regions with temperate and subarctic climates. They inhabit a range of environments, including forests, bogs, and wetlands. These frogs are known for their adaptability and ability to thrive in cold and forested areas.",
        "predators": "Wood Frogs have a variety of predators, including snakes, birds, larger amphibians, and small mammals. These frogs are also preyed upon by certain invertebrates. Due to their cryptic coloration, they can often evade predation by blending into their forested surroundings.",
        "diet": "Wood Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates. They are known to consume prey such as ants, beetles, and other arthropods.",
        "lifespan": "In the wild, Wood Frogs typically have a lifespan of 2 to 3 years, although some individuals may live longer under favorable conditions.",
        "toxicity": "Wood Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
        "interesting_facts": "Wood Frogs are well adapted to their cold habitats and can endure freezing temperatures during hibernation. They enter a state of hibernation in the winter months, where their bodies can freeze and then thaw when they awaken in the spring. These frogs have a relatively wide distribution range across North America, and they are often found in forested areas with access to suitable breeding sites. The ability of Wood Frogs to tolerate freezing temperatures is due to the production of a cryoprotectant substance that prevents ice formation within their cells. This adaptation allows them to survive in cold climates."
    },
    "Poison Dart Frog (Dendrobatidae family)": {
        "description": "The size of Poison Dart Frogs varies depending on the species. They can range from as small as 0.5 inches (1.3 centimeters) to about 2.4 inches (6 centimeters) in length.",
        "habitat": "Poison Dart Frogs are primarily found in Central and South America, inhabiting various rainforests, tropical forests, and other humid and lush environments. Their distribution varies based on the specific species.",
        "predators": "Predators of Poison Dart Frogs can include certain snakes, birds, and larger amphibians. However, not all species in the family are toxic, and some non-toxic species lack potent skin toxins. The toxicity of Poison Dart Frogs is generally associated with their diet in the wild.",
        "diet": "Poison Dart Frogs are insectivorous and primarily feed on a diet consisting of small invertebrates. They are known to consume a variety of prey, including ants, termites, beetles, and other small arthropods.",
        "lifespan": "The lifespan of Poison Dart Frogs can vary by species but is typically several years in the wild. In captivity, they can live longer under suitable conditions.",
        "toxicity": "Many species of Poison Dart Frogs are highly toxic, and their skin secretes potent toxins. These toxins are used as a defense mechanism to deter potential predators. Indigenous peoples in their native regions have used these toxins to poison the tips of blowdarts for hunting, hence the name 'dart frog.' The level of toxicity can vary among species, and not all members of the family are toxic. Captive-bred Poison Dart Frogs often lack the same level of toxicity as their wild counterparts because their diet in captivity is different.",
        "interesting_facts": "Some species of Poison Dart Frogs exhibit vibrant and striking coloration, which is thought to be a warning to potential predators about their toxicity. The toxins of Poison Dart Frogs are believed to come from their diet in the wild, particularly ants and other small arthropods. In captivity, when they are not exposed to the same diet, they may lose their toxicity. Poison Dart Frogs are known for their complex social behaviors and vocalizations, which are used for communication and territorial purposes."
    },
    "Red-eyed Tree Frog (Agalychnis callidryas)": {
        "description": "Red-eyed Tree Frogs are relatively small, typically ranging from about 2 to 2.5 inches (5 to 7 centimeters) in length.",
        "habitat": "These tree frogs are primarily found in the lowland rainforests and tropical jungles of Central America, including countries like Mexico, Costa Rica, Nicaragua, and Honduras. They are arboreal and spend most of their lives in the trees.",
        "predators": "The primary predators of Red-eyed Tree Frogs include various birds, snakes, and larger amphibians. These frogs rely on their vibrant coloration and unique markings as a form of aposematism, which is a warning signal to potential predators.",
        "diet": "Red-eyed Tree Frogs are insectivores and primarily feed on a diet of small invertebrates, such as crickets, flies, moths, and other small arthropods.",
        "lifespan": "In the wild, Red-eyed Tree Frogs typically have a lifespan of about 5 years. However, they may live longer in captivity under suitable conditions.",
        "toxicity": "Red-eyed Tree Frogs are not considered highly poisonous or toxic like some other frog species. Their skin does secrete a mild toxin, but it is generally not dangerous to humans. Their bright colors are more of a warning to predators that they are not safe to eat.",
        "interesting_facts": "Red-eyed Tree Frogs are known for their striking and vibrant appearance, with their bright green bodies, blue flanks, orange toes, and, of course, their large, bright red eyes. They have specialized toe pads that help them cling to leaves and branches in the trees. These toe pads are lined with tiny adhesive disks. Red-eyed Tree Frogs are nocturnal, meaning they are most active at night. During the day, they rest on leaves with their eyes closed to conserve energy and hide from potential predators. Mating rituals of Red-eyed Tree Frogs are quite interesting, involving calling to attract mates, amplexus (the mating embrace), and the male fertilizing the eggs as the female lays them on leaves overhanging water."
    },
    "Purple Frog (Nasikabatrachus sahyadrensis)": {
        "description": "Purple Frogs are relatively large and robust frogs. They typically grow to about 2.0 to 2.5 inches (5 to 6.3 centimeters) in length.",
        "habitat": "These frogs are endemic to the Western Ghats in India, specifically in the states of Kerala and Karnataka. They are primarily found in the Western Ghats' high-altitude regions, which are montane grasslands and shola forests.",
        "predators": "As adult frogs, they have limited natural predators due to their underground and burrowing lifestyle. However, they may face threats from certain ground-dwelling animals like snakes and small mammals. Their underground lifestyle keeps them well-hidden.",
        "diet": "Purple Frogs are burrowing frogs and primarily feed on subterranean prey like termites and ants. Their specialized diet is well-suited for their underground lifestyle.",
        "lifespan": "The lifespan of Purple Frogs in the wild is not well-documented, but they likely have a relatively long lifespan, possibly several years.",
        "toxicity": "Purple Frogs are not known to be poisonous or toxic. Their adaptation to burrowing and the underground environment makes them less exposed to potential predators. Their skin is not known to secrete toxins.",
        "interesting_facts": "Purple Frogs are known for their unique and peculiar appearance. They have a stout, bloated body with a purplish-brown coloration. They have a wrinkled and tubular body shape, which is an adaptation for their burrowing lifestyle. These frogs are fossorial, meaning they spend most of their lives underground. They emerge briefly during the monsoon season to breed. Purple Frogs are famous for their unusual and loud calls, which are often described as 'mooing' sounds. These vocalizations play a significant role in their breeding behavior. They are an ancient and primitive frog species, and their lineage is estimated to be over 100 million years old."
    }
]

# Initialize frog items
def initFrogItems():
    # Set up frog items into a dictionary with id, item, likes, dislikes
    item_id = 0
    for item in frog_item_list:
        frog_items_data.append({"id": item_id, "item": item, "likes": 0, "dislikes": 0})
        item_id += 1
    # Prime some like responses
    for _ in range(10):
        id = getRandomFrogItem()['id']
        addFrogItemLike(id)
    # Prime some dislike responses
    for _ in range(5):
        id = getRandomFrogItem()['id']
        addFrogItemDislike(id)

# Return all frog items from frog_items_data
def getFrogItems():
    return frog_items_data

# Frog item getter
def getFrogItem(id):
    return frog_items_data[id]

# Return a random frog item from frog_items_data
def getRandomFrogItem():
    return random.choice(frog_items_data)

# Most liked frog item
def favoriteFrogItem():
    best = 0
    bestID = -1
    for frog_item in getFrogItems():
        if frog_item['likes'] > best:
            best = frog_item['likes']
            bestID = frog_item['id']
    return frog_items_data[bestID]

# Least appreciated frog item
def dislikedFrogItem():
    worst = 0
    worstID = -1
    for frog_item in getFrogItems():
        if frog_item['dislikes'] > worst:
            worst = frog_item['dislikes']
            worstID = frog_item['id']
    return frog_items_data[worstID]

# Add to likes for a requested id
def addFrogItemLike(id):
    frog_items_data[id]['likes'] = frog_items_data[id]['likes'] + 1
    return frog_items_data[id]['likes']

# Add to dislikes for a requested id
def addFrogItemDislike(id):
    frog_items_data[id]['dislikes'] = frog_items_data[id]['dislikes'] + 1
    return frog_items_data[id]['dislikes']

# Number of frog items
def countFrogItems():
    return len(frog_items_data)

# Pretty Print frog item
def printFrogItem(frog_item):
    print(frog_item['id'], frog_item['item'], "\n", "Likes:", frog_item['likes'], "\n", "Dislikes:", frog_item['dislikes'], "\n")

# Test Frog Item Model
if __name__ == "__main__": 
    initFrogItems()  # initialize frog items

    # Most liked and least liked frog items
    best = favoriteFrogItem()
    print("Most liked:")
    printFrogItem(best)
    worst = dislikedFrogItem()
    print("Least liked:")
    printFrogItem(worst)

    # Random frog item
    print("Random frog item:")
    printFrogItem(getRandomFrogItem())

    # Count of frog items
    print("Frog Items Count: " + str(countFrogItems()))
