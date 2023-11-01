from __init__ import db
frogs_data = []

# frog_list = [
#     {
#         "name": "Sumaco Horned Frog (Hemiphractus proboscideus)",
#         "description": "The Sumaco Horned Frog is medium-sized, typically reaching a size of around 1.5 to 2 inches (3.8 to 5 centimeters).",
#         "habitat": "The Sumaco Horned Frog is native to the cloud forests of Ecuador in South America. It is found in the Sumaco Volcano area, which is its namesake.",
#         "predators": "Predators of the Sumaco Horned Frog may include snakes and certain birds that inhabit the same region.",
#         "diet": "Sumaco Horned Frogs primarily feed on insects and small invertebrates in their natural habitat.",
#         "lifespan": "The typical lifespan of the Sumaco Horned Frog in the wild is around 8 to 10 years.",
#         "toxicity": "The Sumaco Horned Frog is not considered highly poisonous or toxic. It does not possess the potent skin toxins seen in some other frog species.",
#         "interesting_facts": "The Sumaco Horned Frog gets its name from the distinctive bony horn-like protrusions above its eyes, which give it a unique appearance...",
#     },
#     {
#         "name": "Peruvian Toad (Rhinella peruviana)",
#         "description": "Peruvian Toads are medium to large-sized amphibians, typically reaching a size of around 2.4 to 4 inches (6 to 10 centimeters) in length.",
#         "habitat": "Peruvian Toads are found in various countries in South America, including Peru, Ecuador, and Bolivia. They inhabit a range of environments, including tropical rainforests and montane forests...",
#         "predators": "Predators of the Peruvian Toad may include snakes, large birds, and some mammals. They may also face threats from human activities, such as habitat destruction...",
#         "diet": "Peruvian Toads are primarily insectivorous, and they feed on a diet consisting of a variety of insects and other invertebrates...",
#         "lifespan": "The average lifespan of the Peruvian Toad in the wild is not precisely documented but is estimated to be around 5 to 10 years...",
#         "toxicity": "The Peruvian Toad is a species known for its warty skin and distinctive coloration...",
#         "interesting_facts": "The Peruvian Toad is part of the unique and diverse amphibian fauna of South America, and it contributes to the ecosystem by controlling insect populations...",
#     },
#     {
#         "name": "Painted Burrowing Frog (Neobatrachus sudellae)",
#         "description": "The Painted Burrowing Frog is a small-sized frog, typically ranging from about 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length...",
#         "habitat": "The Painted Burrowing Frog is native to the southwestern regions of Western Australia. It is adapted to semi-arid and arid environments and can be found in sandy soils and heathland...",
#         "predators": "Predators of the Painted Burrowing Frog can include snakes, birds, larger amphibians, and various reptiles that share its habitat...",
#         "diet": "Painted Burrowing Frogs primarily feed on small invertebrates, including insects and other arthropods. They are known to eat ants, beetles, and other similar prey...",
#         "lifespan": "The lifespan of the Painted Burrowing Frog in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more...",
#         "toxicity": "The Painted Burrowing Frog is not known to be poisonous or toxic. It lacks the skin toxins found in some other frog species...",
#         "interesting_facts": "The Painted Burrowing Frog gets its name from its distinctive marbled or painted appearance on its skin...",
#     },
#     {
#         "name": "Lao Newt (Tylototriton lauhachindai)",
#         "description": "The Lao Newt is a relatively small amphibian, typically measuring about 5 to 6 inches (12.5 to 15 centimeters) in length...",
#         "habitat": "The Lao Newt is native to Laos and is primarily found in the mountainous regions of northern and central Laos. They inhabit cool, clear, and fast-flowing streams and small rivers...",
#         "predators": "Predators of the Lao Newt may include various aquatic and semi-aquatic predators, such as larger fish, snakes, and some bird species...",
#         "diet": "Lao Newts are carnivorous and primarily feed on aquatic invertebrates, such as small crustaceans, insects, and other small prey that they can capture in their aquatic habitat...",
#         "lifespan": "The lifespan of the Lao Newt in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more...",
#         "toxicity": "The Lao Newt is known to be toxic. Like other newt species, it possesses skin toxins that can be harmful to potential predators...",
#         "interesting_facts": "The Lao Newt is part of the salamander family and is known for its distinctive coloration, with bright orange-red markings...",
#     },
#     {
#         "name": "Eastern Spadefoot Toad (Scaphiopus holbrookii)",
#         "description": "The Eastern Spadefoot Toad is a relatively small amphibian, typically ranging from 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length...",
#         "habitat": "The Eastern Spadefoot Toad is native to the eastern and southeastern regions of the United States, where it can be found in sandy or loamy soils, including pine forests, grasslands, and scrub habitats...",
#         "predators": "Predators of the Eastern Spadefoot Toad can include various snakes, birds, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates...",
#         "diet": "Eastern Spadefoot Toads are insectivorous, primarily feeding on a diet of insects and other arthropods...",
#         "lifespan": "The typical lifespan of Plains Leopard Frogs in the wild is around 2 to 4 years, although this can vary based on environmental conditions and predation...",
#         "toxicity": "Eastern Spadefoot Toads are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species...",
#         "interesting_facts": "These frogs get their name from the spots and blotchy patterns on their skin, resembling a leopard's spots...",
#     },
#     {
#         "name": "Painted Reed Frog (Hyperolius marmoratus)",
#         "description": "The Painted Reed Frog is a small-sized frog, typically ranging from about 0.8 to 1.2 inches (2 to 3 centimeters) in length...",
#         "habitat": "The Painted Reed Frog is native to sub-Saharan Africa and is found in various countries across the continent...",
#         "predators": "Predators of the Painted Reed Frog may include various birds, snakes, small mammals, and other amphibians...",
#         "diet": "Painted Reed Frogs are insectivorous and primarily feed on a diet of small insects and invertebrates...",
#         "lifespan": "The average lifespan of the Painted Reed Frog in the wild is not extensively documented but is estimated to be several years...",
#         "toxicity": "The Painted Reed Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species...",
#         "interesting_facts": "The Painted Reed Frog is known for its striking and colorful markings, which can vary in pattern and coloration...",
#     },
#     {
#         "name": "Malagasy Rainbow Frog (Scaphiophryne gottlebei)",
#         "description": "The Malagasy Rainbow Frog is a small to medium-sized frog, typically ranging from about 1.2 to 1.8 inches (3 to 4.5 centimeters) in length...",
#         "habitat": "The Malagasy Rainbow Frog is native to Madagascar, an island nation off the southeastern coast of Africa...",
#         "predators": "Predators of the Malagasy Rainbow Frog can include various snakes, birds, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates...",
#         "diet": "Malagasy Rainbow Frogs are insectivorous and primarily feed on a diet of insects and other invertebrates...",
#         "lifespan": "The average lifespan of the Malagasy Rainbow Frog in the wild is not extensively documented but is estimated to be several years...",
#         "toxicity": "The Malagasy Rainbow Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species...",
#         "interesting_facts": "The Malagasy Rainbow Frog is named for its striking and colorful patterns, which can vary among individuals...",
#     },
#     {
#         "name": "Hourglass Tree Frog (Dendropsophus ebraccatus)",
#         "description": "The Hourglass Tree Frog is a small-sized frog, typically ranging from about 1 to 1.5 inches (2.5 to 3.8 centimeters) in length...",
#         "habitat": "This species is commonly found in the tropical rainforests of Central America and northern South America...",
#         "predators": "Predators of the Hourglass Tree Frog can include snakes, birds, larger amphibians, and various small mammals. They may also be preyed upon by certain invertebrates...",
#         "diet": "Hourglass Tree Frogs primarily feed on a diet of small insects and invertebrates, including ants, flies, and other arthropods...",
#         "lifespan": "The average lifespan of the Hourglass Tree Frog is around 5 years"
#     }
#      {
#         "name": "Sumaco Horned Frog (Hemiphractus proboscideus)",
#         "description": "The Sumaco Horned Frog is medium-sized, typically reaching a size of around 1.5 to 2 inches (3.8 to 5 centimeters).",
#         "habitat": "The Sumaco Horned Frog is native to the cloud forests of Ecuador in South America. It is found in the Sumaco Volcano area, which is its namesake.",
#         "predators": "Predators of the Sumaco Horned Frog may include snakes and certain birds that inhabit the same region.",
#         "diet": "Sumaco Horned Frogs primarily feed on insects and small invertebrates in their natural habitat.",
#         "lifespan": "The typical lifespan of the Sumaco Horned Frog in the wild is around 8 to 10 years.",
#         "toxicity": "The Sumaco Horned Frog is not considered highly poisonous or toxic. It does not possess the potent skin toxins seen in some other frog species.",
#         "interesting_facts": "The Sumaco Horned Frog gets its name from the distinctive bony horn-like protrusions above its eyes, which give it a unique appearance. These frogs have a cryptic coloration, often resembling moss or lichen, helping them blend into their forest environment. They are known for their unique reproductive behavior, with males guarding eggs and tadpoles, which they carry on their backs. This species is native to a specific and limited geographic range, making it an interesting subject of study and conservation concern."
#     },
#     {
#         "name": "Peruvian Toad (Rhinella peruviana)",
#         "description": "Peruvian Toads are medium to large-sized amphibians, typically reaching a size of around 2.4 to 4 inches (6 to 10 centimeters) in length.",
#         "habitat": "Peruvian Toads are found in various countries in South America, including Peru, Ecuador, and Bolivia. They inhabit a range of environments, including tropical rainforests and montane forests.",
#         "predators": "Predators of the Peruvian Toad may include snakes, large birds, and some mammals. They may also face threats from human activities, such as habitat destruction.",
#         "diet": "Peruvian Toads are primarily insectivorous, and they feed on a diet consisting of a variety of insects and other invertebrates. Their diet may include ants, beetles, and other small arthropods.",
#         "lifespan": "The average lifespan of the Peruvian Toad in the wild is not precisely documented but is estimated to be around 5 to 10 years.",
#         "toxicity": "Peruvian Toads, like many toad species, secrete toxins through their skin, which can act as a defense against predators. However, these toxins can vary among individuals and may not be as potent as those of some other toad species.",
#         "interesting_facts": "Peruvian Toads are adapted to a life in the trees and are often found perched on branches and leaves. They have a distinctive appearance and are known for their unique vocalizations during the breeding season."
#     },
#     {
#         "name": "Painted Burrowing Frog (Neobatrachus sudellae)",
#         "description": "The Painted Burrowing Frog is a small-sized frog, typically ranging from about 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length.",
#         "habitat": "The Painted Burrowing Frog is native to the southwestern regions of Western Australia. It is adapted to semi-arid and arid environments and can be found in sandy soils and heathland.",
#         "predators": "Predators of the Painted Burrowing Frog can include snakes, birds, larger amphibians, and various reptiles that share its habitat.",
#         "diet": "Painted Burrowing Frogs primarily feed on small invertebrates, including insects and other arthropods. They are known to eat ants, beetles, and other similar prey.",
#         "lifespan": "The lifespan of the Painted Burrowing Frog in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more.",
#         "toxicity": "The Painted Burrowing Frog is not known to be poisonous or toxic. It lacks the skin toxins found in some other frog species.",
#         "interesting_facts": "The Painted Burrowing Frog gets its name from its distinctive marbled or painted appearance on its skin."
#     },
#     {
#         "name": "Plains Leopard Frog (Lithobates blairi)",
#         "description": "Plains Leopard Frogs are medium-sized frogs, typically ranging from about 2 to 3 inches (5 to 7.6 centimeters) in length.",
#         "habitat": "These frogs are found in a variety of habitats, including grasslands, prairies, wetlands, and semi-aquatic environments. They are native to parts of North America, including the Great Plains region.",
#         "predators": "Predators of Plains Leopard Frogs may include snakes, birds, larger amphibians, and various small mammals. Additionally, they may face threats from certain invertebrates.",
#         "diet": "Plains Leopard Frogs are insectivorous and primarily feed on a diet of insects, spiders, and other small invertebrates.",
#         "lifespan": "The typical lifespan of Plains Leopard Frogs in the wild is around 2 to 4 years, although this can vary based on environmental conditions and predation.",
#         "toxicity": "Plains Leopard Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
#         "interesting_facts": "These frogs get their name from the spots and blotchy patterns on their skin, resembling a leopard's spots. They are known for their distinctive vocalizations during the breeding season, which sound like chuckling laughter. Plains Leopard Frogs are adapted to a variety of terrestrial and aquatic habitats, and they often inhabit grasslands and wetlands with temporary or semi-permanent water bodies. During the breeding season, males call from the water to attract females for mating."
#     },
#     {
#         "name": "Coorg Yellow Bush Frog (Raorchestes luteolus)",
#         "description": "Coorg Yellow Bush Frogs are relatively small frogs, typically measuring about 1.2 to 1.6 inches (3 to 4 centimeters) in length.",
#         "habitat": "These frogs are native to the Western Ghats region of India, particularly in the Coorg region. They inhabit dense vegetation, including bushes and shrubs, in forested and hilly areas.",
#         "predators": "Predators of Coorg Yellow Bush Frogs may include snakes, larger insects, and various birds.",
#         "diet": "Coorg Yellow Bush Frogs primarily feed on small insects and arthropods that they can find in their natural habitat.",
#         "lifespan": "The average lifespan of Coorg Yellow Bush Frogs in the wild is not extensively documented but is estimated to be several years.",
#         "toxicity": "Coorg Yellow Bush Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
#         "interesting_facts": "These frogs have a bright yellow coloration, which helps them blend into the vegetation of their habitat. Coorg Yellow Bush Frogs are known for their distinctive calls, which are often heard during the breeding season. These calls help them communicate and locate potential mates. They are adapted to an arboreal (tree-dwelling) lifestyle and are often found perched on leaves and branches. The species is native to a region with rich biodiversity, and it contributes to the local ecosystem by controlling insect populations."
#     },
#     {
#         "name": "Starry Night Reed Frog (Hyperolius pusillus)",
#         "description": "Starry Night Reed Frogs are small-sized frogs, typically ranging from about 0.8 to 1.2 inches (2 to 3 centimeters) in length.",
#         "habitat": "These frogs are native to sub-Saharan Africa and are found in various countries across the continent. They inhabit a range of environments, including savannas, grasslands, and reed beds near freshwater sources.",
#         "predators": "Predators of Starry Night Reed Frogs may include various birds, snakes, small mammals, and other amphibians. They are vulnerable to a variety of animals that share their habitat.",
#         "diet": "Starry Night Reed Frogs are insectivorous and primarily feed on a diet of small insects and invertebrates. They are known to consume prey such as small flies and other arthropods.",
#         "lifespan": "The average lifespan of Starry Night Reed Frogs in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
#         "toxicity": "Starry Night Reed Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
#         "interesting_facts": "The Starry Night Reed Frog is known for its striking and colorful markings, which can vary in pattern and coloration. These patterns are often used for camouflage in their reed bed habitats. They have a unique breeding behavior, with males calling from the vegetation near water to attract females for mating. Starry Night Reed Frogs are well adapted to their freshwater environments and are excellent climbers, often found clinging to vegetation near water. These frogs are relatively small and have a charming, colorful appearance, making them a popular subject for amphibian enthusiasts and photographers."
#     },
#     {
#         "name": "Yellow-striped Poison Dart Frog (Dendrobates truncatus)",
#         "description": "Yellow-striped Poison Dart Frogs are typically small, with an average length of about 1 to 1.5 inches (2.5 to 4 centimeters).",
#         "habitat": "They are primarily found in the tropical rainforests of South America, particularly in countries like Brazil and Peru. These frogs are often associated with lowland rainforests and can be found near small streams, ponds, and other water sources.",
#         "predators": "While they are small and brightly colored, these frogs are highly toxic, which serves as a defense mechanism against predators. However, certain snake species and some birds have developed a resistance to their toxins and may prey on them.",
#         "diet": "Yellow-striped Poison Dart Frogs primarily feed on small arthropods, including ants, termites, mites, and other small invertebrates. Their diet plays a crucial role in the development of their toxic skin secretions.",
#         "lifespan": "In the wild, their lifespan is not extensively documented, but it is estimated to be several years. In captivity, with proper care, they can live for more extended periods.",
#         "toxicity": "These frogs are indeed poisonous. They get their name from the toxic secretions on their skin, which can be harmful or even deadly to potential predators. Indigenous people have used the toxins from these frogs to poison the tips of blowdarts for hunting.",
#         "interesting_facts": "These frogs are known for their bright and striking coloration, which can vary among individuals. The vibrant colors act as a warning signal to potential predators. Indigenous people of South America have used the toxins from these frogs for centuries to poison their blowdarts, which is why they are called 'dart frogs.' Their toxicity is believed to be a result of their diet, as they obtain certain alkaloids from the arthropods they consume."
#     }
# ]

class FrogSpecies(db.Model):
    __tablename__ = "FrogSpecies"
    name = db.Column(db.String, primary_Key=True)
    size = db.Column(db.String, primary_Key=True)
    habitat = db.Column(db.String, primary_Key=True)
    predators = db.Column(db.String, primary_Key=True)
    diet = db.Column(db.String, primary_Key=True)
    lifespan = db.Column(db.String, primary_Key=True)
    toxicity = db.Column(db.String, primary_Key=True)
    fun_facts = db.Column(db.String, primary_Key=True)
#    image = db.Column(db.String, primary_key=True) 
    db.Column(db.Integer, primary_key=True)
    def __init__(self, name, size, habitat, predators, diet, lifespan, toxicity, fun_facts):
        self.name = name
        self.size = size
        self.habitat = habitat
        self.predators = predators
        self.diet = diet
        self.lifespan = lifespan
        self.toxicity = toxicity
        self.fun_facts = fun_facts
#        self.image = image

    def to_dict(self):
        return {"name": self.name, "size": self.size, "habitat": self.habitat, "predators": self.predators, "diet": self.size, "lifespan": self.lifespan, "toxicity": self.toxicity, "fun_facts": self.toxicity}


def initFrogs():
    exists = FrogSpecies.query.filter_by(name = "Plains Leopard Frog (Lithobates blairi)").first()
    if not exists: 
        frog1 = FrogSpecies(name="Plains Leopard Frog (Lithobates blairi)", size="Plains Leopard Frogs are medium-sized frogs, typically ranging from about 2 to 3 inches (5 to 7.6 centimeters) in length.", habitat="These frogs are found in a variety of habitats, including grasslands, prairies, wetlands, and semi-aquatic environments. They are native to parts of North America, including the Great Plains region.", predators="Predators of Plains Leopard Frogs may include snakes, birds, larger amphibians, and various small mammals. Additionally, they may face threats from certain invertebrates.", diet="Plains Leopard Frogs are insectivorous and primarily feed on a diet of insects, spiders, and other small invertebrates.", lifespan="The typical lifespan of Plains Leopard Frogs in the wild is around 2 to 4 years, although this can vary based on environmental conditions and predation.", toxicity="Plains Leopard Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.", fun_facts="These frogs get their name from the spots and blotchy patterns on their skin, resembling a leopard's spots. They are known for their distinctive vocalizations during the breeding season, which sound like chuckling laughter. Plains Leopard Frogs are adapted to a variety of terrestrial and aquatic habitats, and they often inhabit grasslands and wetlands with temporary or semi-permanent water bodies. During the breeding season, males call from the water to attract females for mating.")
        db.session.add(frog1)
    exists = FrogSpecies.query.filter_by(name = "Sumaco Horned Frog (Hemiphractus proboscideus)").first()
    if not exists: 
        frog2 = FrogSpecies(name="Sumaco Horned Frog (Hemiphractus proboscideus)", size="The Sumaco Horned Frog is medium-sized, typically reaching a size of around 1.5 to 2 inches (3.8 to 5 centimeters).", habitat="The Sumaco Horned Frog is native to the cloud forests of Ecuador in South America. It is found in the Sumaco Volcano area, which is its namesake.", predators="Predators of the Sumaco Horned Frog may include snakes and certain birds that inhabit the same region.", diet="Sumaco Horned Frogs primarily feed on insects and small invertebrates in their natural habitat.", lifespan="The typical lifespan of the Sumaco Horned Frog in the wild is around 8 to 10 years.", toxicity="The Sumaco Horned Frog is not considered highly poisonous or toxic. It does not possess the potent skin toxins seen in some other frog species.", fun_facts="The Sumaco Horned Frog gets its name from the distinctive bony horn-like protrusions above its eyes, which give it a unique appearance.These frogs have a cryptic coloration, often resembling moss or lichen, helping them blend into their forest environment. They are known for their unique reproductive behavior, with males guarding eggs and tadpoles, which they carry on their backs. This species is native to a specific and limited geographic range, making it an interesting subject of study and conservation concern.")
        db.session.add(frog2)
    exists = FrogSpecies.query.filter_by(name = "Peruvian Toad (Rhinella peruviana)").first() 
    if not exists:
        frog3 = FrogSpecies(name="Peruvian Toad (Rhinella peruviana)", size="Peruvian Toads are medium to large-sized amphibians, typically reaching a size of around 2.4 to 4 inches (6 to 10 centimeters) in length.", habitat="Peruvian Toads are found in various countries in South America, including Peru, Ecuador, and Bolivia. They inhabit a range of environments, including tropical rainforests and montane forests.", predators="Predators of the Peruvian Toad may include snakes, large birds, and some mammals. They may also face threats from human activities, such as habitat destruction.", diet="Peruvian Toads are primarily insectivorous, and they feed on a diet consisting of a variety of insects and other invertebrates. Their diet may include ants, beetles, and other small arthropods.", lifespan="The average lifespan of the Peruvian Toad in the wild is not precisely documented but is estimated to be around 5 to 10 years.", toxicity="Peruvian Toads, like many toad species, secrete toxins through their skin. These toxins can be harmful or even deadly to predators that attempt to consume them. However, the level of toxicity can vary among individuals and is often more pronounced in certain regions or populations.", fun_facts="The Peruvian Toad is a species known for its warty skin and distinctive coloration, which can help it blend into its environment. As with many toad species, the toxins they secrete from their skin glands serve as a defense mechanism against potential predators. Toads, including the Peruvian Toad, have specialized parotoid glands behind their eyes that release toxins when threatened. These toads are important components of their ecosystems and contribute to insect population control due to their diet.",)
        db.session.add(frog3)
    exists = FrogSpecies.query.filter_by(name = "American Bullfrog (Lithobates catesbeianus").first()
    if not exists:
        frog4 = FrogSpecies(size="American Bullfrogs are one of the largest frog species and can reach lengths of up to 6 to 8 inches (15 to 20 centimeters) or even larger.", habitat="These frogs are native to North America and are found in a wide range of aquatic habitats, including ponds, lakes, slow-moving rivers, and marshes. They are highly adaptable and can thrive in both natural and man-made water bodies", predators="While American Bullfrogs are large and less vulnerable to predation as adults, their tadpoles and young frogs are susceptible to predation by a variety of aquatic animals, including fish, birds, snakes, and even other bullfrogs.", diet="Bullfrogs are voracious predators and eat a wide range of prey, including insects, other smaller frogs, fish, small mammals, and even birds. They are known for their powerful jaws and the ability to consume prey items nearly as large as themselves.", lifespan="In the wild, American Bullfrogs can live for several years, typically around 7 to 9 years. Their lifespan may vary depending on factors like habitat quality and predation.", toxicity="American Bullfrogs are not considered poisonous or toxic to humans. However, they do have a set of powerful jaws and sharp teeth, so handling them can result in a painful bite. It's also worth noting that the skin of amphibians like the American Bullfrog can secrete toxins, but these are not typically harmful to humans.", fun_facts="The American Bullfrog is known for its distinctive 'jug-o'-rum' call, which is a loud, resonant, and repetitive sound produced by the males during the breeding season. They have a unique and characteristic olive-green coloration with a light-colored belly. American Bullfrogs are considered invasive species in some regions where they have been introduced. Their large size and voracious appetite can have negative impacts on local ecosystems, especially when they outcompete native species. Bullfrogs are powerful swimmers and are capable of leaping great distances when attempting to escape predators.") 
    db.session.add(frog4)
    exists = FrogSpecies.query.filter_by(name = "Red-eyed Tree Frog (Agalychnis callidryas)").first()
    if not exists:
        frog5 = FrogSpecies(size="Red-eyed Tree Frogs are relatively small, typically ranging from about 2 to 2.5 inches (5 to 7 centimeters) in length.", habitat= "These tree frogs are primarily found in the lowland rainforests and tropical jungles of Central America, including countries like Mexico, Costa Rica, Nicaragua, and Honduras. They are arboreal and spend most of their lives in the trees.", predators= "The primary predators of Red-eyed Tree Frogs include various birds, snakes, and larger amphibians. These frogs rely on their vibrant coloration and unique markings as a form of aposematism, which is a warning signal to potential predators.", diet="Red-eyed Tree Frogs are insectivores and primarily feed on a diet of small invertebrates, such as crickets, flies, moths, and other small arthropods.", lifespan="In the wild, Red-eyed Tree Frogs typically have a lifespan of about 5 years. However, they may live longer in captivity under suitable conditions.", toxicity= "Red-eyed Tree Frogs are not considered highly poisonous or toxic like some other frog species. Their skin does secrete a mild toxin, but it is generally not dangerous to humans. Their bright colors are more of a warning to predators that they are not safe to eat.", fun_facts="Red-eyed Tree Frogs are known for their striking and vibrant appearance, with their bright green bodies, blue flanks, orange toes, and, of course, their large, bright red eyes. They have specialized toe pads that help them cling to leaves and branches in the trees. These toe pads are lined with tiny adhesive disks. Red-eyed Tree Frogs are nocturnal, meaning they are most active at night. During the day, they rest on leaves with their eyes closed to conserve energy and hide from potential predators. Mating rituals of Red-eyed Tree Frogs are quite interesting, involving calling to attract mates, amplexus (the mating embrace), and the male fertilizing the eggs as the female lays them on leaves overhanging water.")
    db.session.add(frog5)
    exists = FrogSpecies.query.filter_by(name = "Poison Dart Frog (Dendrobatidae family)").first()
    if not exists:
        frog6 = FrogSpecies(size="The size of Poison Dart Frogs varies depending on the species. They can range from as small as 0.5 inches (1.3 centimeters) to about 2.4 inches (6 centimeters) in length.", habitat="Poison Dart Frogs are primarily found in Central and South America, inhabiting various rainforests, tropical forests, and other humid and lush environments. Their distribution varies based on the specific species.", predators="Predators of Poison Dart Frogs can include certain snakes, birds, and larger amphibians. However, not all species in the family are toxic, and some non-toxic species lack potent skin toxins. The toxicity of Poison Dart Frogs is generally associated with their diet in the wild.", diet= "Poison Dart Frogs are insectivorous and primarily feed on a diet consisting of small invertebrates. They are known to consume a variety of prey, including ants, termites, beetles, and other small arthropods.", lifespan= "The lifespan of Poison Dart Frogs can vary by species but is typically several years in the wild. In captivity, they can live longer under suitable conditions.", toxicity="Many species of Poison Dart Frogs are highly toxic, and their skin secretes potent toxins. These toxins are used as a defense mechanism to deter potential predators. Indigenous peoples in their native regions have used these toxins to poison the tips of blowdarts for hunting, hence the name 'dart frog.' The level of toxicity can vary among species, and not all members of the family are toxic. Captive-bred Poison Dart Frogs often lack the same level of toxicity as their wild counterparts because their diet in captivity is different.", fun_facts= "Some species of Poison Dart Frogs exhibit vibrant and striking coloration, which is thought to be a warning to potential predators about their toxicity. The toxins of Poison Dart Frogs are believed to come from their diet in the wild, particularly ants and other small arthropods. In captivity, when they are not exposed to the same diet, they may lose their toxicity. Poison Dart Frogs are known for their complex social behaviors and vocalizations, which are used for communication and territorial purposes.")
    db.session.add(frog6)
    exists = FrogSpecies.query.filter_by(name = "Tomato Frog (Dyscophus species)").first()
    if not exists:
        frog7 = FrogSpecies(size="Tomato Frogs are relatively small to medium-sized frogs, typically ranging from about 2 to 4 inches (5 to 10 centimeters) in length, depending on the species and age.", habitat="Tomato Frogs are native to Madagascar, an island nation off the southeastern coast of Africa. They inhabit various environments on the island, including rainforests, swamps, and wetlands. They are often associated with shallow, slow-moving bodies of water.", predators= "Predators of Tomato Frogs can include various birds, snakes, larger amphibians, and some mammals. Their bright coloration serves as a warning to potential predators that they may be toxic, deterring them from attempting to consume the frogs.", diet= "Tomato Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates found in their wetland and forest habitats. They may consume ants, termites, and other small arthropods.", lifespan="The lifespan of Tomato Frogs in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.", toxicity="Tomato Frogs are known for their skin toxins, which can be harmful to potential predators. The bright red or orange coloration is an aposematic warning to predators, signaling their toxicity. When threatened, they can secrete a milky substance from their skin that contains toxins, causing irritation or harm to potential predators.", fun_facts= "Tomato Frogs are named for their vibrant red or orange coloration, which resembles a ripe tomato. This bright color serves as a warning to predators that they are toxic, and their skin secretions can be harmful. They have a robust and heavy build compared to some other frogs, which contributes to their distinctive appearance. Tomato Frogs are known for their explosive breeding behavior, which often occurs after heavy rainfall. Males call loudly to attract females, and they lay their eggs in temporary pools of water where tadpoles develop.")
    db.session.add(frog7)
    exists = FrogSpecies.query.filter_by(name = "Green Tree Frog (Hyla cinerea)").first()
    if not exists:
        frog8 = FrogSpecies(size= "Green Tree Frogs are relatively small, with sizes typically ranging from 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length. They have a slender build with bright green skin, although their coloration can vary.", habitat= "These frogs are found in a variety of habitats, including swamps, marshes, forests, and urban areas, throughout the southeastern United States. They are often associated with wetlands and are excellent climbers, typically residing in trees and shrubs.", predators= "Natural predators of Green Tree Frogs include various birds, snakes, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates.", diet= "Green Tree Frogs are insectivorous and primarily feed on a diet of insects, spiders, and other small invertebrates. They are known for their ability to capture prey with their long, sticky tongues.", lifespan= "In the wild, Green Tree Frogs typically have a lifespan of 5 to 10 years, depending on factors such as environmental conditions and predation.", toxicity= "Green Tree Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.", fun_facts= "Green Tree Frogs are known for their vibrant green coloration, which serves as camouflage in their leafy habitats. They are excellent climbers and can often be found clinging to vegetation near water sources. These frogs are often heard at night, producing a distinctive and pleasant-sounding call, which can vary by region. Green Tree Frogs are adaptable and can thrive in various environments, including urban areas with suitable habitats.")
    db.session.add(frog8)
    exists = FrogSpecies.query.filter_by(name = "Goliath Frog (Conraua goliath)").first()
    if not exists:
        frog9 = FrogSpecies(size= "The Goliath Frog is one of the largest frog species in the world. Adult Goliath Frogs can reach a length of up to 12.6 inches (32 centimeters) and weigh up to 3.3 kilograms (7.3 pounds). Tadpoles of this species can also grow to substantial sizes.", habitat= "Goliath Frogs are native to the rainforests of Central and West Africa, specifically found in the regions of Equatorial Guinea and Cameroon. They inhabit fast-flowing rivers and streams within the dense rainforest, preferring areas with rocky substrates.", predators= "Despite their impressive size, Goliath Frogs have some natural predators. Their primary predators include large water birds, such as herons, and various aquatic predators. Additionally, humans pose a threat due to habitat destruction and over-harvesting.", diet= "Goliath Frogs are opportunistic carnivores, primarily feeding on a diet of insects, small vertebrates, and invertebrates that they can capture near the water's edge. They are known to consume a variety of prey, including insects, crabs, and small fish.", lifespan= "The exact lifespan of Goliath Frogs in the wild is not well-documented, but they are believed to live several years. In captivity, they may live longer, potentially up to 15 years.", toxicity= "Goliath Frogs are not known to be poisonous or toxic in the same way some other frog species are. They rely more on their size and camouflage for protection.", fun_facts= "Goliath Frogs are the world's largest frogs, both in terms of size and weight. Their massive appearance and size distinguish them from most other frog species. They have a remarkable and unique breeding behavior, where the male frogs call loudly to attract females. The female Goliath Frogs lay their eggs in or near fast-flowing rivers, and the male guards the eggs and tadpoles until they metamorphose into froglets. The large size of Goliath Frogs is thought to be an adaptation to the fast-flowing streams they inhabit. Their size helps them withstand the strong currents and maintain their position within the water. Goliath Frogs have a greenish-brown coloration with mottled patterns on their skin, which provides excellent camouflage in their lush rainforest environment.")
    db.session.add(frog9)
    exists = FrogSpecies.query.filter_by(name = "Glass Frog (Centrolenidae family)").first()
    if not exists:
        frog10 = FrogSpecies(size="The size of Glass Frogs varies depending on the species. They typically range from around 1 to 3 inches (2.5 to 7.5 centimeters) in length.", habitat="Glass Frogs are primarily found in the rainforests and cloud forests of Central and South America, particularly in countries like Costa Rica, Panama, Colombia, Ecuador, and others. They are arboreal, which means they spend much of their time in the trees and vegetation near streams and rivers.", predators= "Predators of Glass Frogs can include various birds, snakes, larger amphibians, and some mammals. Their semi-transparent skin can make them vulnerable to visual predators, but their green coloration helps with camouflage.", diet="Glass Frogs are insectivorous, primarily feeding on a diet of insects and other small invertebrates found in their rainforest habitat.", lifespan= "The lifespan of Glass Frogs in the wild varies by species but is estimated to be several years, typically up to 5 years or more, depending on environmental conditions and predation.", toxicity= "While many species of frogs are known for their skin toxins, Glass Frogs are generally not considered highly poisonous or toxic. They lack the potent skin toxins found in some other frog families.", fun_facts= "The primary distinguishing feature of Glass Frogs is their translucent skin, which allows you to see their internal organs, including the heart, liver, and gastrointestinal tract. These frogs are known for their unique breeding behavior. Males often guard and protect their eggs, which they attach to the undersides of leaves hanging over streams. This protects the eggs from aquatic predators.")
    db.session.add(frog10)
    db.session.commit()
