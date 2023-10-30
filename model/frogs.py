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
        "lifespan": "The average lifespan of the Hourglass Tree Frog is around 5 years
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
