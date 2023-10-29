import threading

# import "packages" from flask
from flask import render_template, jsonify  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers


# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.player import player_api


# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(player_api)
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():    
    return render_template("table.html")

class FrogSpecies:
    def __init__(self, name, size, habitat, predators, diet, lifespan, toxicity, fun_facts):
        self.name = name
        self.size = size
        self.habitat = habitat
        self.predators = predators
        self.diet = diet
        self.lifespan = lifespan
        self.toxicity = toxicity
        self.fun_facts = fun_facts

    def print_info(self):
        print(f"Species: {self.name}")
        print(f"Size: {self.size}")
        print(f"Habitat: {self.habitat}")
        print(f"Predators: {self.predators}")
        print(f"Diet: {self.diet}")
        print(f"Lifespan: {self.lifespan}")
        print(f"Toxicity: {self.toxicity}")
        print(f"Fun Facts: {self.fun_facts}")
        print('----------------------------------------')
        
    def to_dict(self):
        dict = {}
        dict["Species"] = self.name
        dict["Size"] = self.size
        dict["Habitat"] = self.habitat
        dict["Predators"] = self.predators
        dict["Diet"] = self.diet
        dict["Lifespan"] = self.lifespan
        dict["Toxicity"] = self.toxicity
        dict["Fun Facts"] = self.fun_facts
        return dict
    
frog_species_list = []

def addFrogSpecies(name, size, habitat, predators, diet, lifespan, toxicity, fun_facts):
    frog = FrogSpecies(name, size, habitat, predators, diet, lifespan, toxicity, fun_facts)
    frog_species_list.append(frog.to_dict())

addFrogSpecies(
    "Sumaco Horned Frog (Hemiphractus proboscideus)", 
    "The Sumaco Horned Frog is medium-sized, typically reaching a size of around 1.5 to 2 inches (3.8 to 5 centimeters).",
    "The Sumaco Horned Frog is native to the cloud forests of Ecuador in South America. It is found in the Sumaco Volcano area, which is its namesake.",
    "Predators of the Sumaco Horned Frog may include snakes and certain birds that inhabit the same region.",
    "Sumaco Horned Frogs primarily feed on insects and small invertebrates in their natural habitat.",
    "The typical lifespan of the Sumaco Horned Frog in the wild is around 8 to 10 years.",
    "The Sumaco Horned Frog is not considered highly poisonous or toxic. It does not possess the potent skin toxins seen in some other frog species.",
    "The Sumaco Horned Frog gets its name from the distinctive bony horn-like protrusions above its eyes, which give it a unique appearance.These frogs have a cryptic coloration, often resembling moss or lichen, helping them blend into their forest environment. They are known for their unique reproductive behavior, with males guarding eggs and tadpoles, which they carry on their backs. This species is native to a specific and limited geographic range, making it an interesting subject of study and conservation concern.",
)

addFrogSpecies(
    "Peruvian Toad (Rhinella peruviana)",
    "Peruvian Toads are medium to large-sized amphibians, typically reaching a size of around 2.4 to 4 inches (6 to 10 centimeters) in length.",
    "Peruvian Toads are found in various countries in South America, including Peru, Ecuador, and Bolivia. They inhabit a range of environments, including tropical rainforests and montane forests.",
    "Predators of the Peruvian Toad may include snakes, large birds, and some mammals. They may also face threats from human activities, such as habitat destruction.",
    "Peruvian Toads are primarily insectivorous, and they feed on a diet consisting of a variety of insects and other invertebrates. Their diet may include ants, beetles, and other small arthropods.",
    "The average lifespan of the Peruvian Toad in the wild is not precisely documented but is estimated to be around 5 to 10 years.",
    "Peruvian Toads, like many toad species, secrete toxins through their skin. These toxins can be harmful or even deadly to predators that attempt to consume them. However, the level of toxicity can vary among individuals and is often more pronounced in certain regions or populations.",
    "The Peruvian Toad is a species known for its warty skin and distinctive coloration, which can help it blend into its environment. As with many toad species, the toxins they secrete from their skin glands serve as a defense mechanism against potential predators. Toads, including the Peruvian Toad, have specialized parotoid glands behind their eyes that release toxins when threatened. These toads are important components of their ecosystems and contribute to insect population control due to their diet.",
)

addFrogSpecies(
    "Painted Burrowing Frog (Neobatrachus sudellae)",
    "The Painted Burrowing Frog is a small-sized frog, typically ranging from about 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length.",
    "The Painted Burrowing Frog is native to the southwestern regions of Western Australia. It is adapted to semi-arid and arid environments and can be found in sandy soils and heathland.",
    "Predators of the Painted Burrowing Frog can include snakes, birds, larger amphibians, and various reptiles that share its habitat.",
    "Painted Burrowing Frogs primarily feed on small invertebrates, including insects and other arthropods. They are known to eat ants, beetles, and other similar prey.",
    "The lifespan of the Painted Burrowing Frog in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more, depending on environmental conditions and predation.",
    "The Painted Burrowing Frog is not known to be poisonous or toxic. It lacks the skin toxins found in some other frog species.",
    "The Painted Burrowing Frog gets its name from its distinctive marbled or painted appearance on its skin, which can vary in color and pattern. This species is well adapted to its arid habitat and is known for burrowing into the sandy soils to escape extreme temperatures and conserve moisture. They have a unique burrowing behavior, spending much of their lives underground, emerging during periods of heavy rain for breeding. These frogs are relatively small and have a charming, unassuming appearance.",
)

addFrogSpecies(
    "Lao Newt (Tylototriton lauhachindai)",
    "The Lao Newt is a relatively small amphibian, typically measuring about 5 to 6 inches (12.5 to 15 centimeters) in length.",
    "The Lao Newt is native to Laos and is primarily found in the mountainous regions of northern and central Laos. It inhabits cool, clear, and fast-flowing streams and small rivers.",
    "Predators of the Lao Newt may include various aquatic and semi-aquatic predators, such as larger fish, snakes, and some bird species.",
    "Lao Newts are carnivorous and primarily feed on aquatic invertebrates, such as small crustaceans, insects, and other small prey that they can capture in their aquatic habitat.",
    "The lifespan of the Lao Newt in the wild is not extensively documented but is estimated to be several years, possibly up to a decade or more.",
    "The Lao Newt is known to be toxic. Like other newt species, it possesses skin toxins that can be harmful to potential predators. These toxins serve as a defense mechanism to deter predation.",
    "The Lao Newt is part of the salamander family and is known for its distinctive coloration, with bright orange-red markings on a dark background. This species is listed as endangered due to habitat loss and degradation, making it a conservation concern. Lao Newts are adapted to cool, fast-flowing streams and are excellent swimmers. The toxicity of these newts is attributed to compounds known as tetrodotoxins, which can be found in their skin and other tissues. These toxins are the same ones found in pufferfish and are highly potent.",
)

addFrogSpecies(
    "Eastern Spadefoot Toad (Scaphiopus holbrookii)",
    "The Eastern Spadefoot Toad is a relatively small amphibian, typically ranging from 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length.",
    "The Eastern Spadefoot Toad is native to the eastern and southeastern regions of the United States, where it can be found in sandy or loamy soils, including pine forests, grasslands, and scrub habitats.",
    "Predators of the Eastern Spadefoot Toad can include various snakes, birds, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates.",
    "Eastern Spadefoot Toads are insectivorous, primarily feeding on a diet of insects and other arthropods. They are known to consume a variety of small prey, including ants, termites, and beetles.",
    "The Eastern Spadefoot Toad typically has a lifespan of 5 to 10 years in the wild, depending on environmental conditions and predation.",
    "The Eastern Spadefoot Toad is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog and toad species.",
    "Eastern Spadefoot Toads get their name from a keratinized, spade-like projection on their hind feet, which they use for burrowing. This adaptation helps them survive in sandy soils. They are known for their unique breeding behavior, which is often triggered by heavy rains. They lay their eggs in temporary pools of water. Eastern Spadefoot Toads are primarily nocturnal, coming out at night to forage for food and engage in their breeding activities. These toads are adapted to arid and sandy habitats and can endure dry conditions by burrowing underground, where they can remain for long periods.",
)

addFrogSpecies(
    "Painted Reed Frog (Hyperolius marmoratus)",
    "The Painted Reed Frog is a small-sized frog, typically ranging from about 0.8 to 1.2 inches (2 to 3 centimeters) in length.",
    "The Painted Reed Frog is native to sub-Saharan Africa and is found in various countries across the continent. They inhabit a range of environments, including savannas, grasslands, and reed beds near freshwater sources.",
    "Predators of the Painted Reed Frog may include various birds, snakes, small mammals, and other amphibians. They are vulnerable to a variety of animals that share their habitat.",
    "Painted Reed Frogs are insectivorous and primarily feed on a diet of small insects and invertebrates. They are known to consume prey such as small flies and other arthropods.",
    "The average lifespan of the Painted Reed Frog in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
    "The Painted Reed Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species.",
    "The Painted Reed Frog is known for its striking and colorful markings, which can vary in pattern and coloration. These patterns are often used for camouflage in their reed bed habitats. They have a unique breeding behavior, with males calling from the vegetation near water to attract females for mating. Painted Reed Frogs are well adapted to their freshwater environments and are excellent climbers, often found clinging to vegetation near water. These frogs are relatively small and have a charming, colorful appearance, making them a popular subject for amphibian enthusiasts and photographers.",
)

addFrogSpecies(
    "Malagasy Rainbow Frog (Scaphiophryne gottlebei)",
    "The Malagasy Rainbow Frog is a small to medium-sized frog, typically ranging from about 1.2 to 1.8 inches (3 to 4.5 centimeters) in length.",
    "The Malagasy Rainbow Frog is native to Madagascar, an island nation off the southeastern coast of Africa. They inhabit a variety of environments on the island, including dry deciduous forests and spiny thickets.",
    "Predators of the Malagasy Rainbow Frog can include various snakes, birds, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates.",
    "Malagasy Rainbow Frogs are insectivorous and primarily feed on a diet of insects and other invertebrates. They are known to consume a variety of small prey, including ants, termites, and beetles.",
    "The average lifespan of the Malagasy Rainbow Frog in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
    "The Malagasy Rainbow Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species.",
    "The Malagasy Rainbow Frog is named for its striking and colorful patterns, which can vary among individuals. They exhibit a combination of red, orange, and yellow colors on a dark background. This species is found only in Madagascar and is part of the unique and diverse amphibian fauna of the island. They have a distinctive sit-and-wait feeding behavior, where they remain still and ambush prey that comes within range. Malagasy Rainbow Frogs are adapted to both terrestrial and arboreal (tree-dwelling) habitats, making them a fascinating and adaptable species.",
)

addFrogSpecies(
    "Hourglass Tree Frog (Dendropsophus ebraccatus)",
    "The Hourglass Tree Frog is a small-sized frog, typically ranging from about 1 to 1.5 inches (2.5 to 3.8 centimeters) in length.",
    "This species is commonly found in the tropical rainforests of Central America and northern South America. It prefers habitats near water bodies like ponds, streams, and marshes.",
    "Predators of the Hourglass Tree Frog can include snakes, birds, larger amphibians, and various small mammals. They may also be preyed upon by certain invertebrates.",
    "Hourglass Tree Frogs primarily feed on a diet of small insects and invertebrates, including ants, flies, and other arthropods.",
    "The average lifespan of the Hourglass Tree Frog in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
    "The Hourglass Tree Frog is not known to be highly poisonous or toxic. It lacks the potent skin toxins found in some other frog species.",
    "These frogs are known for their distinctive hourglass-shaped pattern on their backs, which gives them their common name. Hourglass Tree Frogs have sticky toe pads that help them climb and stick to vegetation. They are arboreal, spending most of their time in trees and shrubs. Males of this species are known for their loud, high-pitched calls during the breeding season to attract females.",
)

addFrogSpecies(
    "Plains Leopard Frog (Lithobates blairi)",
    "Plains Leopard Frogs are medium-sized frogs, typically ranging from about 2 to 3 inches (5 to 7.6 centimeters) in length.",
    "These frogs are found in a variety of habitats, including grasslands, prairies, wetlands, and semi-aquatic environments. They are native to parts of North America, including the Great Plains region.",
    "Predators of Plains Leopard Frogs may include snakes, birds, larger amphibians, and various small mammals. Additionally, they may face threats from certain invertebrates.",
    "Plains Leopard Frogs are insectivorous and primarily feed on a diet of insects, spiders, and other small invertebrates.",
    "The typical lifespan of Plains Leopard Frogs in the wild is around 2 to 4 years, although this can vary based on environmental conditions and predation.",
    "Plains Leopard Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
    "These frogs get their name from the spots and blotchy patterns on their skin, resembling a leopard's spots. They are known for their distinctive vocalizations during the breeding season, which sound like chuckling laughter. Plains Leopard Frogs are adapted to a variety of terrestrial and aquatic habitats, and they often inhabit grasslands and wetlands with temporary or semi-permanent water bodies. During the breeding season, males call from the water to attract females for mating.",
)

addFrogSpecies(
    "Coorg Yellow Bush Frog (Raorchestes luteolus)",
    "Coorg Yellow Bush Frogs are relatively small frogs, typically measuring about 1.2 to 1.6 inches (3 to 4 centimeters) in length.",
    "These frogs are native to the Western Ghats region of India, particularly in the Coorg region. They inhabit dense vegetation, including bushes and shrubs, in forested and hilly areas.",
    "Predators of Coorg Yellow Bush Frogs may include snakes, larger insects, and various birds.",
    "Coorg Yellow Bush Frogs primarily feed on small insects and arthropods that they can find in their natural habitat.",
    "The average lifespan of Coorg Yellow Bush Frogs in the wild is not extensively documented but is estimated to be several years.",
    "Coorg Yellow Bush Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
    "These frogs have a bright yellow coloration, which helps them blend into the vegetation of their habitat. Coorg Yellow Bush Frogs are known for their distinctive calls, which are often heard during the breeding season. These calls help them communicate and locate potential mates. They are adapted to an arboreal (tree-dwelling) lifestyle and are often found perched on leaves and branches. The species is native to a region with rich biodiversity, and it contributes to the local ecosystem by controlling insect populations.",
)

addFrogSpecies(
    "Starry Night Reed Frog (Hyperolius pusillus)",
    "Starry Night Reed Frogs are small-sized frogs, typically ranging from about 0.8 to 1.2 inches (2 to 3 centimeters) in length.",
    "These frogs are native to sub-Saharan Africa and are found in various countries across the continent. They inhabit a range of environments, including savannas, grasslands, and reed beds near freshwater sources.",
    "Predators of Starry Night Reed Frogs may include various birds, snakes, small mammals, and other amphibians. They are vulnerable to a variety of animals that share their habitat.",
    "Starry Night Reed Frogs are insectivorous and primarily feed on a diet of small insects and invertebrates. They are known to consume prey such as small flies and other arthropods.",
    "The average lifespan of Starry Night Reed Frogs in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
    "Starry Night Reed Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
    "The Starry Night Reed Frog is known for its striking and colorful markings, which can vary in pattern and coloration. These patterns are often used for camouflage in their reed bed habitats. They have a unique breeding behavior, with males calling from the vegetation near water to attract females for mating. Starry Night Reed Frogs are well adapted to their freshwater environments and are excellent climbers, often found clinging to vegetation near water. These frogs are relatively small and have a charming, colorful appearance, making them a popular subject for amphibian enthusiasts and photographers.",
)

addFrogSpecies(
    "Yellow-striped Poison Dart Frog (Dendrobates truncatus)",
    "Yellow-striped Poison Dart Frogs are typically small, with an average length of about 1 to 1.5 inches (2.5 to 4 centimeters).",
    "They are primarily found in the tropical rainforests of South America, particularly in countries like Brazil and Peru. These frogs are often associated with lowland rainforests and can be found near small streams, ponds, and other water sources.",
    "While they are small and brightly colored, these frogs are highly toxic, which serves as a defense mechanism against predators. However, certain snake species and some birds have developed a resistance to their toxins and may prey on them.",
    "Yellow-striped Poison Dart Frogs primarily feed on small arthropods, including ants, termites, mites, and other small invertebrates. Their diet plays a crucial role in the development of their toxic skin secretions.",
    "In the wild, their lifespan is not extensively documented, but it is estimated to be several years. In captivity, with proper care, they can live for more extended periods.",
    "These frogs are indeed poisonous. They get their name from the toxic secretions on their skin, which can be harmful or even deadly to potential predators. Indigenous people have used the toxins from these frogs to poison the tips of blowdarts for hunting.",
    "These frogs are known for their bright and striking coloration, which can vary among individuals. The vibrant colors act as a warning signal to potential predators. Indigenous people of South America have used the toxins from these frogs for centuries to poison their blowdarts, which is why they are called 'dart frogs.' Their toxicity is believed to be a result of their diet, as they obtain certain alkaloids from the arthropods they consume.",
)

addFrogSpecies(
    "Archey's Frog (Leiopelma archeyi)",
    "Archey's Frogs are small amphibians, with adults measuring about 3 to 4.4 centimeters (1.2 to 1.7 inches) in length. They have a compact and robust body structure.",
    "These frogs are endemic to New Zealand and are found on the North Island. They inhabit cool, moist, and dense forest environments, often near streams and wetlands. They are particularly associated with areas of high rainfall.",
    "While adult Archey's Frogs have few natural predators, invasive species like rats, stoats, and other introduced mammals pose a significant threat to their eggs and tadpoles. Invasive species have led to a decline in their population.",
    "Archey's Frogs are primarily insectivorous, with a diet consisting of small invertebrates like insects, spiders, and other arthropods. They are known for their slow feeding behavior.",
    "In the wild, their lifespan can extend up to 30 years, making them one of the longest-lived frogs known. This longevity is remarkable for a small amphibian.",
    "Archey's Frogs are not known to be poisonous or toxic. They lack the potent skin toxins found in some other frog species. Instead, their main defense strategy is their cryptic appearance and living in remote, hard-to-reach habitats.",
    "These frogs have a limited range and are often considered 'living fossils' because they have changed very little over millions of years of evolution. They belong to an ancient lineage of frogs. They are often referred to as 'pepeketua' in the Māori language, which translates to 'the night creeper,' referencing their nocturnal habits. Archey's Frogs have a distinctive appearance, with rough, granular skin that helps with camouflage in their forested habitat.",
)

addFrogSpecies(
    "Red-legged Frog (Rana aurora)",
    "Red-legged Frogs are considered relatively large for a frog species, with adults typically reaching sizes of 5.5 to 11 centimeters (2.2 to 4.3 inches) in length.",
    "They are found in a variety of habitats, including freshwater bodies like ponds, lakes, marshes, and slow-moving streams. They are also known to inhabit terrestrial environments near aquatic habitats. Red-legged Frogs are primarily found in the western United States and southwestern Canada.",
    "The Red-legged Frog faces predation from a variety of animals, including birds, mammals, snakes, larger amphibians, and some invertebrates like insects. Introduced fish species can also be a threat to their eggs and tadpoles.",
    "Red-legged Frogs are carnivorous and primarily feed on a diet of insects, small invertebrates, and even smaller vertebrates. Their diet may include various insects, spiders, worms, and other small prey items found in their aquatic and terrestrial habitats.",
    "In the wild, Red-legged Frogs can have a lifespan of up to 8 years or more. Their longevity can vary depending on environmental conditions, predation, and other factors.",
    "While they are not as poisonous as some other frog species, Red-legged Frogs do secrete mild toxins through their skin, which can make them unpalatable to some predators. However, their level of toxicity is not as potent as, for example, poison dart frogs.",
    "Red-legged Frogs are often recognized by their distinct red coloration on the undersides of their hind legs, which gives them their name. They are excellent jumpers and swimmers, capable of leaping great distances and navigating through aquatic environments. Red-legged Frogs are known for their distinct, resonant call, which is often described as sounding like 'jug-o-rum'. They are considered an ecologically important species, playing a role in regulating insect populations and serving as prey for various predators in their habitat.",
)

addFrogSpecies(
    "European Common Frog (Rana temporaria)",
    "European Common Frogs are relatively small to medium-sized frogs, with adults typically ranging from 6 to 9 centimeters (2.4 to 3.5 inches) in length.",
    "These frogs are widespread across Europe and can be found in a variety of habitats, including woodlands, grasslands, wetlands, gardens, and urban areas. They are known for their adaptability to different environments.",
    "Predators of the European Common Frog can include a range of animals such as birds, snakes, larger amphibians, and some mammals. They may also face threats from various invertebrates. These frogs are an important food source for many animals in their ecosystems.",
    "European Common Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates. Their diet may include ants, flies, beetles, and other similar prey items.",
    "In the wild, European Common Frogs typically have a lifespan of about 4 to 8 years, although their longevity can vary based on environmental conditions and threats.",
    "European Common Frogs are not considered highly poisonous or toxic. They do not possess the potent skin toxins seen in some other frog species. However, they can secrete mild toxins, making them less palatable to predators.",
    "European Common Frogs are known for their unique call, which is often heard during the breeding season. The males produce a sound similar to a soft 'ribbit' to attract females. They have a wide range of color variations, including brown, green, and even reddish tones, depending on their surroundings and environmental conditions. During the winter, these frogs hibernate in protected sites, such as leaf litter and underground burrows, to survive the cold temperatures.",
)

addFrogSpecies(
    "Oriental Fire-bellied Toad (Bombina orientalis)",
    "Oriental Fire-bellied Toads are relatively small in size, typically ranging from 3.2 to 5.5 centimeters (1.3 to 2.2 inches) in length.",
    "These toads are native to a wide range of habitats, including various regions in Asia. They are commonly found in wetland areas, such as ponds, marshes, and slow-moving streams. They are well adapted to both terrestrial and aquatic environments.",
    "Predators of the Oriental Fire-bellied Toad may include snakes, birds, larger amphibians, and some mammals. These toads have developed a unique defense mechanism. When threatened, they arch their bodies and display their brightly colored bellies as a warning signal to potential predators.",
    "Oriental Fire-bellied Toads are primarily insectivorous and feed on a diet of small invertebrates. They consume a variety of prey, including insects, spiders, and other small arthropods.",
    "In the wild, Oriental Fire-bellied Toads can live for an average of 5 to 10 years, although this can vary based on environmental conditions and predation.",
    "These toads are mildly toxic. They have skin glands that secrete toxins, which are not usually deadly but can be irritating to potential predators or even humans if the toads are handled. However, their bright coloration serves as a warning to deter predators.",
    "Oriental Fire-bellied Toads are known for their vibrant green and black coloration on their dorsal side and bright orange or red markings on their ventral side. This coloration serves as aposematism, a warning signal to potential predators. When threatened, these toads may secrete a milky substance from their skin that contains toxins, serving as a defense mechanism. They are semi-aquatic and have webbed feet, which are well-suited for swimming and hopping in and around water bodies. Oriental Fire-bellied Toads are often kept as pets due to their striking appearance and relatively simple care requirements in a captive environment.",
)

addFrogSpecies(
    "White-lipped Tree Frog (Litoria infrafrenata)",
    "White-lipped Tree Frogs are relatively large frogs, with an average length ranging from 10 to 12.5 centimeters (4 to 5 inches).",
    "These frogs are native to a variety of regions, particularly in Papua New Guinea and parts of northern Australia. They are well adapted to arboreal (tree-dwelling) habitats and are often found near freshwater sources in rainforests and other wooded areas.",
    "Predators of the White-lipped Tree Frog may include various birds, snakes, large insects, and some mammals. Being a tree-dwelling species, they are less vulnerable to aquatic predators.",
    "White-lipped Tree Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates. They are known to consume a variety of prey, including moths, flies, and other arthropods.",
    "In the wild, these frogs can have a lifespan of up to 16 years, but the average lifespan may vary based on environmental conditions and predation.",
    "White-lipped Tree Frogs are not considered highly poisonous or toxic. They do not have the potent skin toxins seen in some other frog species.",
    "White-lipped Tree Frogs are known for their striking appearance, with bright green coloration on their dorsal side and a distinctive white stripe along their upper lip, which gives them their name. They are excellent climbers and have adhesive toe pads that allow them to cling to vegetation and move about trees and shrubs. These frogs often inhabit the canopy of rainforests, where they lay their eggs in leaves that collect rainwater, creating small water-filled pools for their tadpoles to develop. White-lipped Tree Frogs are known for their loud and distinctive calls, which are used by males to attract females during the breeding season.",
)

addFrogSpecies(
    "Brazilian Horned Frog (Ceratophrys aurita)",
    "Brazilian Horned Frogs are relatively large, with adults typically ranging from 10 to 15 centimeters (4 to 6 inches) in length, although some individuals can grow even larger.",
    "They are native to South America, primarily found in countries like Brazil and Uruguay. Brazilian Horned Frogs inhabit a range of environments, including tropical rainforests and wetlands. They are known to burrow in the ground, where they spend much of their time.",
    "Predators of Brazilian Horned Frogs may include birds, larger amphibians, snakes, and mammals. These frogs have a unique defense mechanism, using their wide mouth and powerful jaws to ambush and consume potential threats, including small vertebrates.",
    "Brazilian Horned Frogs are carnivorous and known for their voracious appetites. They primarily feed on insects, small vertebrates, and other prey that they can capture, thanks to their large mouth and quick strikes.",
    "In the wild, Brazilian Horned Frogs can live for an average of 5 to 10 years, although their lifespan may vary based on environmental conditions and the availability of food.",
    "Brazilian Horned Frogs are not considered highly poisonous or toxic in the same way some other frog species are. They do not possess potent skin toxins.",
    "Brazilian Horned Frogs get their name from the pointed, horn-like structures above their eyes, which give them a distinctive appearance. They are often referred to as 'Pacman frogs' due to their large mouth and round body shape. These frogs are sit-and-wait predators. They remain hidden in the leaf litter or soil, waiting for prey to come close, and then they strike with remarkable speed to capture their meal. Brazilian Horned Frogs are known for their adaptability to various environments and can be found in both pristine and disturbed habitats.",
)

addFrogSpecies(
    "Amazon Milk Frog (Trachycephalus resinifictrix)",
    "Amazon Milk Frogs are medium-sized frogs, typically ranging from about 2 to 3 inches (5 to 7.5 centimeters) in length.",
    "They are native to South America and can be found in countries like Brazil, Peru, and Colombia. Amazon Milk Frogs inhabit various environments, including rainforests, tropical lowlands, and wetlands. They are often found near freshwater sources.",
    "Predators of the Amazon Milk Frog may include various birds, snakes, and other amphibians. They may also face threats from larger insects and invertebrates. Their bright coloration is a warning signal to potential predators.",
    "Amazon Milk Frogs are insectivorous and primarily feed on a diet of insects and small invertebrates. They consume prey such as small flies, crickets, moths, and other arthropods.",
    "In the wild, Amazon Milk Frogs can live for up to 10 years or more, depending on environmental conditions and predation. Their lifespan can be influenced by factors such as habitat quality and availability of food.",
    "Amazon Milk Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species. However, they have a unique defense mechanism: when threatened, they excrete a milky secretion from their skin, which is a defensive strategy to deter predators.",
    "Amazon Milk Frogs are known for their vibrant green coloration, which serves as camouflage in their leafy habitats. Their bellies are typically creamy white. When threatened, they excrete a sticky, milky substance from their skin, giving them their common name 'Milk Frog.' These frogs are arboreal, meaning they spend a significant amount of time in trees and vegetation. Amazon Milk Frogs are skilled climbers, often found clinging to leaves and branches near water sources.",
)

addFrogSpecies(
    "Bumblebee Poison Dart Frog (Dendrobates leucomelas)",
    "The Bumblebee Poison Dart Frog is a small frog, typically ranging from about 1 to 2 inches (2.5 to 5 centimeters) in length.",
    "These frogs are native to South America and are found in countries like Venezuela, Colombia, and Brazil. They inhabit tropical rainforests and dense vegetation near freshwater sources like streams and small rivers.",
    "Despite their small size, Bumblebee Poison Dart Frogs have very few natural predators. This is because they are highly toxic. Their bright colors serve as a warning to potential predators. Only a few species in their habitat have developed immunity to their toxins.",
    "These frogs are insectivorous and primarily feed on a diet of small arthropods and insects. Their diet may include ants, termites, small beetles, and other tiny invertebrates.",
    "In the wild, Bumblebee Poison Dart Frogs have a relatively long lifespan for a frog, typically living up to 5-7 years or more. In captivity, where they are not exposed to natural predators and stressors, they can live even longer.",
    "Bumblebee Poison Dart Frogs are among the most toxic animals on Earth. They secrete potent neurotoxins through their skin, which can be deadly to potential predators. Indigenous people, such as the native tribes of South America, have been known to use the toxins from these frogs to poison the tips of blowdarts for hunting. However, in captivity, when they are not exposed to the same insects they would consume in the wild, they do not develop these toxins.",
    "Bumblebee Poison Dart Frogs are named for their distinctive black and yellow coloration, which resembles the colors of a bumblebee. This bold coloration serves as a warning to potential predators about their toxicity. The toxic compounds they secrete are known as batrachotoxins, and they are among the most potent natural toxins. Female Bumblebee Poison Dart Frogs lay their eggs in leaf litter on the forest floor. Once hatched, the female transports her tadpoles to small water-filled cavities in plants. These frogs are known for their intricate courtship rituals, which often involve calling and various body movements.",
)

addFrogSpecies(
    "Green and Black Poison Dart Frog (Dendrobates auratus)",
    "The Green and Black Poison Dart Frog is a small-sized frog, typically ranging from 3 to 5 centimeters (1.2 to 2 inches) in length.",
    "They are native to Central and South America, particularly in tropical rainforests, moist lowland forests, and near streams and rivers.",
    "Natural predators of the Green and Black Poison Dart Frog include various birds, snakes, larger amphibians, and certain mammals.",
    "They are insectivores and primarily feed on a variety of small invertebrates, including ants, beetles, and other insects.",
    "In the wild, they can live for about 3 to 6 years. In captivity with proper care, they may live up to 10 years or more.",
    "As the name suggests, the Green and Black Poison Dart Frog is highly toxic. They possess potent skin toxins, particularly batrachotoxin, which is one of the most toxic substances known to humans.",
    "The bright coloration of this frog serves as a warning to potential predators about their toxicity. Indigenous people have used the toxins from these frogs to coat the tips of blowdarts for hunting, giving them the name dart frogs. They are known for their complex social behaviors, including courtship rituals and territorial defense.",
)

addFrogSpecies(
    "Pine Barrens Treefrog (Hyla andersonii)",
    "The Pine Barrens Treefrog is a small-sized frog, typically ranging from 2.5 to 5.5 centimeters (1 to 2.2 inches) in length.",
    "They are primarily found in the United States, specifically in the Pine Barrens region of New Jersey. They inhabit wetlands, bogs, swamps, and forested areas with slow-moving water bodies.",
    "Natural predators of the Pine Barrens Treefrog include birds, snakes, larger amphibians, and various mammals.",
    "They are insectivores and primarily feed on a variety of insects, including flies, beetles, ants, and other small invertebrates.",
    "In the wild, Pine Barrens Treefrogs can live for about 3 to 7 years. However, their lifespan may vary depending on environmental factors.",
    "The Pine Barrens Treefrog is not known to be poisonous or toxic to humans.",
    "They are known for their distinctive call, which sounds like a series of honks or quacks, similar to the call of a duck. The Pine Barrens Treefrog is considered a species of special concern due to its limited range and habitat loss. Their coloration helps them blend in with their surroundings, making them well-adapted to their wetland habitats.",
)

addFrogSpecies(
    "Moor Frog (Rana arvalis)",
    "The Moor Frog is a medium-sized frog, typically ranging from 6 to 9 centimeters (2.4 to 3.5 inches) in length.",
    "Moor Frogs are primarily found in Europe, particularly in damp and boggy habitats. They inhabit a variety of wetland environments including marshes, peat bogs, and meadows with seasonal ponds.",
    "The main predators of Moor Frogs include birds (such as herons and gulls), snakes, larger amphibians, and mammals like foxes and martens.",
    "They are insectivores and primarily feed on a variety of insects and invertebrates found in their wetland habitats.",
    "In the wild, Moor Frogs typically live for about 4 to 8 years. However, their lifespan can vary depending on environmental conditions and predation.",
    "Moor Frogs are not considered poisonous or toxic to humans.",
    "Male Moor Frogs are known for their distinctive blue coloration during the breeding season. This blue coloration is temporary and is used to attract females. They are highly adapted to life in wetland habitats and have specialized webbed feet for efficient swimming. Moor Frogs are considered an important species for the health of wetland ecosystems as they help control insect populations.",
)

addFrogSpecies(
    "Western Chorus Frog (Pseudacris triseriata)",
    "The Western Chorus Frog is a small-sized frog, typically ranging from 2.5 to 4 centimeters (1 to 1.6 inches) in length.",
    "Western Chorus Frogs are native to North America and can be found in a wide range of habitats including grasslands, meadows, swamps, and forested areas. They are known for their adaptability to both wet and dry environments.",
    "Natural predators of the Western Chorus Frog include birds (such as herons and owls), snakes, larger amphibians, and various mammals.",
    "They are insectivores and primarily feed on a variety of insects and small invertebrates found in their habitat, including flies, ants, and beetles.",
    "In the wild, Western Chorus Frogs typically live for about 3 to 7 years.",
    "Western Chorus Frogs are not considered poisonous or toxic to humans.",
    "Western Chorus Frogs are known for their distinctive and repetitive calls, which resemble the sound of running a thumbnail along the teeth of a comb. This call is often described as sounding like crreeeek... crreeeek. They are highly adaptable and can thrive in a variety of habitats, making them one of the most widely distributed frogs in North America. These frogs are known for their color variation, which can range from green to brown, depending on factors like temperature and habitat.",
)

addFrogSpecies(
    "Burmese Peacock Frog (Pseudophilautus species)",
    "The Burmese Peacock Frog is a small-sized frog, typically ranging from 2.5 to 3 centimeters (1 to 1.2 inches) in length.",
    "The Burmese Peacock Frog is native to the forests of Myanmar (Burma). They are primarily found in tropical and subtropical rainforests, where they inhabit leaf litter and moist environments.",
    "Predators of the Burmese Peacock Frog may include birds, snakes, larger amphibians, and certain mammals.",
    "They are insectivores and primarily feed on a variety of small invertebrates, including ants, beetles, and other insects found in the leaf litter.",
    "The exact lifespan of the Burmese Peacock Frog in the wild may vary, but it is generally expected to be a few years.",
    "While specific toxicity information for all Pseudophilautus species may not be widely documented, some members of the genus are known to produce skin toxins as a defense mechanism. It is advisable to exercise caution when handling any wild frog, especially if its toxicity is unknown.",
    "The Burmese Peacock Frog gets its name from the vibrant and striking coloration of some species, resembling the colors of a peacock. Many species of the Pseudophilautus genus are known for their unique and melodious calls, which vary between different species.",
)

addFrogSpecies(
    "Parachute Frog (Rhacophorus species)",
    "Parachute Frogs are typically medium-sized frogs, ranging from 4 to 7 centimeters (1.6 to 2.8 inches) in length.",
    "Parachute Frogs are found in various parts of Asia, including countries like India, China, Malaysia, and Indonesia. They inhabit tropical rainforests, often in hilly or mountainous regions, where they are adapted to arboreal (tree-dwelling) lifestyles.",
    "The natural predators of Parachute Frogs include birds of prey, snakes, larger amphibians, and some mammals.",
    "They are insectivores and primarily feed on a variety of insects, including flies, ants, and other small invertebrates found in the forest canopy.",
    "The lifespan of Parachute Frogs can vary among species, but they typically live for several years in the wild, with some reaching up to 10 years or more.",
    "Some species of Parachute Frogs are known to possess skin toxins as a defense mechanism. These toxins can be harmful to predators, and in some cases, even to humans. However, not all species within the genus Rhacophorus are toxic, and the level of toxicity may vary.",
    "Parachute Frogs are named for their unique ability to glide or parachute from tree to tree using specialized webbed feet and skin flaps (patagia) that allow them to catch air and glide. Mating behavior in some species involves the male creating a foam nest on leaves overhanging water. The female lays her eggs in this nest, and the male guards and tends to them until they hatch.",
)

addFrogSpecies(
    "Malaysian Horned Frog (Megophrys nasuta)",
    "The Malaysian Horned Frog is a relatively large frog, with adults typically ranging from 8 to 14 centimeters (3 to 5.5 inches) in length.",
    "These frogs are native to Southeast Asia, including countries like Malaysia, Thailand, Indonesia, and surrounding regions. They are often found in humid tropical rainforests, as well as in grasslands and wetlands.",
    "Predators of the Malaysian Horned Frog may include birds, snakes, larger amphibians, and some mammals.",
    "They are sit-and-wait predators, primarily feeding on a diet of insects and small invertebrates. They are known to consume a wide variety of prey items including insects, spiders, and even small vertebrates.",
    "In the wild, Malaysian Horned Frogs can live for about 7 to 10 years with proper conditions and habitat.",
    "While the Malaysian Horned Frog is not considered highly toxic, they do possess skin toxins as a defense mechanism. These toxins can cause mild irritation or discomfort if they come into contact with mucous membranes or open wounds.",
    "The distinctive horns on their heads are actually bony extensions, known as supraorbital dermal appendages. These structures help them blend into their surroundings by resembling leaf litter or small branches. When threatened, Malaysian Horned Frogs can inflate themselves, making them appear larger and potentially deterring predators.",
)

addFrogSpecies(
    "Mantella Frog (Mantella species)",
    "Mantella Frogs are typically small-sized frogs, ranging from 2.5 to 5 centimeters (1 to 2 inches) in length.",
    "Mantella Frogs are native to Madagascar, an island off the coast of Africa. They are primarily found in tropical rainforests, marshes, and moist lowland areas.",
    "Natural predators of Mantella Frogs include various birds, snakes, larger amphibians, and certain mammals.",
    "They are insectivores and primarily feed on a variety of insects and small invertebrates found in their habitats.",
    "In the wild, Mantella Frogs typically live for about 5 to 8 years. However, their lifespan can vary depending on environmental conditions.",
    "Many species of Mantella Frogs are known to be toxic or poisonous. They have bright and warning coloration, which serves as an indicator of their toxicity to potential predators.",
    "Mantella Frogs are known for their vibrant and striking colors, which can range from bright reds and oranges to blues and yellows. These colors serve as a warning to predators about their toxicity. They are often referred to as Madagascar's poison dart frogs due to their similarity in appearance and toxicity to the poison dart frogs found in Central and South America. Mantella Frogs have a unique and complex courtship behavior, which includes vocalizations and various visual displays.",
)

addFrogSpecies(
    "Greening Frog (Hyla gratiosa)",
    "The Greening Frog, also known as the Barking Treefrog, is a medium-sized frog, typically ranging from 5 to 8 centimeters (2 to 3.1 inches) in length.",
    "They are native to the southeastern United States, including parts of Florida, Georgia, South Carolina, and Alabama. They are typically found in wetland habitats like swamps, marshes, ponds, and slow-moving streams.",
    "Natural predators of the Greening Frog include birds, snakes, larger amphibians, and various mammals.",
    "They are insectivores and primarily feed on a variety of insects and small invertebrates found in their wetland habitats.",
    "In the wild, Greening Frogs typically live for about 3 to 5 years. However, their lifespan can vary depending on environmental conditions and predation.",
    "Greening Frogs are not considered poisonous or toxic to humans.",
    "The Greening Frog gets its name from the vocalization that sounds like a dog's bark or a goose's honk. This distinctive call is most commonly heard during the breeding season. They have adhesive toe pads that allow them to climb and cling to vegetation, making them well-adapted to their arboreal lifestyle.",
)

addFrogSpecies(
    "White's Tree Frog (Litoria caerulea)",
    "White's Tree Frog is a medium to large-sized frog, typically ranging from 10 to 14 centimeters (4 to 5.5 inches) in length.",
    "They are native to northern and eastern parts of Australia, but due to their popularity in the pet trade, they can now be found in various parts of the world. They inhabit a wide range of environments including tropical rainforests, savannas, and even urban areas.",
    "Natural predators of White's Tree Frog include various birds, snakes, and larger amphibians. Additionally, some mammals and large insects may also prey on them.",
    "They are insectivores and primarily feed on a variety of insects such as crickets, cockroaches, moths, and beetles.",
    "In captivity, White's Tree Frogs can live up to 16 years or more with proper care. In the wild, their lifespan is generally shorter due to various environmental factors.",
    "White's Tree Frog is not considered toxic or poisonous to humans.",
    "They are often referred to as dumpy tree frogs due to their plump appearance. White's Tree Frogs have a distinctive, loud, and sometimes shrill call that sounds like a honking horn. They have a unique adaptation that allows them to absorb moisture through their skin, which is particularly useful in arid environments.",
)

addFrogSpecies(
    "Vietnamese Mossy Frog (Theloderma corticale)",
    "Vietnamese Mossy Frogs are relatively small, with adults typically measuring about 2 to 2.5 inches (5 to 6.5 centimeters) in length.",
    "These frogs are native to northern Vietnam and are often found in montane cloud forests and hilly regions. They are well adapted to life in forested areas with dense vegetation, where they can hide among moss and foliage.",
    "While they are not well-documented, potential predators of Vietnamese Mossy Frogs may include snakes, larger amphibians, and some birds. These frogs are cryptic and well-camouflaged, which helps them avoid detection by predators.",
    "Vietnamese Mossy Frogs are insectivorous and primarily feed on a diet of small invertebrates, including insects and arachnids. They use their long, sticky tongues to capture prey.",
    "In the wild, their lifespan is not extensively documented, but it's estimated to be several years, possibly up to a decade or more, depending on environmental conditions and predation.",
    "Vietnamese Mossy Frogs are not known to be poisonous or toxic like some other frog species. They rely on their cryptic coloration and behavior rather than toxins for protection.",
    "The Vietnamese Mossy Frog gets its name from its unique appearance. Their skin is covered in tubercles and irregularly shaped protuberances, giving them a mossy or lichen-like appearance, which serves as camouflage in their forest habitat. These frogs have an unusual breeding behavior. The female lays her eggs in plant leaves overhanging water, and when the tadpoles hatch, they drop into the water below to continue their development. They are primarily arboreal, meaning they spend a significant portion of their lives in trees and shrubs.",
)

addFrogSpecies(
    "Coqui Frog (Eleutherodactylus coqui)",
    "Coqui Frogs are relatively small, typically ranging from about 1 to 2 inches (2.5 to 5 centimeters) in length.",
    "These frogs are native to Puerto Rico, but they have been introduced to other regions, including Hawaii and New Zealand. They are often found in a variety of habitats, including forests, grasslands, gardens, and urban areas. Coqui Frogs have adapted well to human-altered environments.",
    "In their native habitat, Coqui Frogs have several predators, including birds, snakes, and some insects. However, their invasive presence in regions like Hawaii has created ecological imbalances, as they lack natural predators in these areas.",
    "Coqui Frogs are insectivorous and primarily feed on a diet of various small invertebrates, including insects such as ants, flies, and other arthropods.",
    "The lifespan of Coqui Frogs in the wild can vary, but they typically live for several years, with some individuals living up to five years.",
    "Coqui Frogs are not known to be poisonous or toxic. They rely on their ability to blend into their surroundings and their rapid reproductive rate as a survival strategy.",
    "Coqui Frogs are known for their distinctive 'co-qui' call, which is often used to locate other frogs and establish territory. This call can be quite loud and persistent, especially in areas where they have become invasive, causing noise disturbances to local residents. These frogs are known for their high reproductive rate, with females laying large clutches of eggs. Their adaptability to different habitats and rapid reproduction have contributed to their invasive success in some regions. In areas where Coqui Frogs have become invasive, they can have negative ecological impacts on local ecosystems. Their presence can disrupt native ecosystems and threaten native species.",
)

addFrogSpecies(
    "Budgett's Frog (Paraguay Frog, Paratelmatobius cf. poecilogaster)",
    "Budgett's Frogs are relatively large compared to many other frog species, typically reaching sizes of 3 to 4 inches (7.5 to 10 centimeters) in length. They have a distinctive appearance with a flattened body and a 'grinning' mouth, which gives them a distinctive and somewhat comical look.",
    "These frogs are native to South America, specifically regions in Paraguay, Argentina, and Bolivia. They are often found in lowland areas, typically inhabiting marshes, ponds, and wetlands.",
    "Budgett's Frogs have several predators, including snakes, birds, and larger amphibians. Their unique appearance, with a wide mouth and somewhat intimidating appearance, might deter some predators.",
    "These frogs are known to feed on a diet consisting primarily of insects, particularly aquatic insects, small vertebrates, and other prey that they can find in their aquatic habitat.",
    "The precise lifespan of Budgett's Frogs in the wild is not extensively documented, but they can live for several years under suitable conditions, possibly up to a decade or more.",
    "Budgett's Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species, and their defense strategy primarily relies on their appearance.",
    "Budgett's Frogs are known for their distinctive appearance, which includes a wide, grinning mouth. This appearance is often referred to as a 'smiling frog' or 'Paraguay Horned Frog.' Their unique appearance, with a flattened body and mouth, helps them blend into their aquatic environment, making them excellent ambush predators. While not highly poisonous, their appearance might serve as a deterrent to potential predators.",
)

addFrogSpecies(
    "Solomon Island Leaf Frog (Ceratobatrachus guentheri)",
    "These frogs are relatively small, with adults typically ranging from about 1.2 to 2 inches (3 to 5 centimeters) in length.",
    "The Solomon Island Leaf Frog is native to the Solomon Islands in the southwestern Pacific Ocean. They are primarily found in rainforests and are often associated with leaves and vegetation near small streams and other water bodies.",
    "While specific predators of the Solomon Island Leaf Frog aren't extensively documented, they may face threats from various rainforest-dwelling predators, such as snakes, birds, and larger amphibians.",
    "These frogs are insectivorous, primarily feeding on a diet consisting of small insects and invertebrates found in their rainforest habitat.",
    "The precise lifespan of the Solomon Island Leaf Frog in the wild isn't well-documented, but it is estimated to be several years, typically up to 5 years or more, depending on environmental conditions and predation.",
    "The Solomon Island Leaf Frog is not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
    "These frogs are known for their striking green coloration and unique leaf-like appearance, which helps them blend into their rainforest habitat. Their large, webbed feet and the fringed edges of their skin flaps aid in gliding from tree to tree, giving them a unique ability to move through the rainforest canopy. Solomon Island Leaf Frogs are adapted to an arboreal (tree-dwelling) lifestyle and are skilled climbers, often found in vegetation above water.",
)

addFrogSpecies(
    "Paraguay Horned Frog (Ceratophrys cranwelli)",
    "Paraguay Horned Frogs are relatively large amphibians. They can reach sizes of around 3 to 4.7 inches (7.5 to 12 centimeters) in length.",
    "These frogs are native to parts of South America, including Paraguay and Argentina. They inhabit semi-aquatic environments, such as swamps, marshes, and slow-moving water bodies.",
    "Common predators of the Paraguay Horned Frog include various birds, snakes, and larger amphibians. These frogs are ambush predators, and they have a large mouth for capturing prey.",
    "Paraguay Horned Frogs are carnivorous and primarily feed on a diet of insects, small vertebrates, and other prey that they can capture using their impressive, gaping mouth. They are known to eat a variety of creatures, including other frogs, small rodents, and insects.",
    "In the wild, Paraguay Horned Frogs typically have a lifespan of up to 5 to 10 years, depending on environmental conditions and predation.",
    "While these frogs are not typically considered poisonous, they have a defense mechanism involving inflating their bodies when threatened, which can make them less palatable to potential predators. They also have strong jaws and sharp teeth, which can deliver a powerful bite if necessary.",
    "The Paraguay Horned Frog gets its name from the bony, horn-like projections over its eyes, which are believed to serve a defensive purpose. They have a broad mouth and a voracious appetite, often consuming prey nearly the same size as themselves. These frogs are known for their unique and powerful bite, and they are sometimes referred to as 'Pac-Man frogs' because of their mouth size and feeding behavior. Paraguay Horned Frogs are adapted to a semi-aquatic lifestyle and are often found near water. They spend much of their time lying in wait for unsuspecting prey.",
)

addFrogSpecies(
    "Fire-bellied Toad (Bombina species)",
    "Fire-bellied toads are relatively small, with adults typically ranging from 1.2 to 2.4 inches (3 to 6 centimeters) in length.",
    "Fire-bellied toads are native to a broad range of habitats, primarily in Europe and Asia. They can be found in various environments, including forests, grasslands, marshes, and ponds. They are semi-aquatic and often inhabit areas with freshwater.",
    "Predators of Fire-bellied toads can include birds, snakes, larger amphibians, and some mammals. Due to their small size and vibrant coloration, these toads rely on their warning colors to deter potential predators.",
    "Fire-bellied toads are insectivorous and primarily feed on a diet of small invertebrates, such as insects and other arthropods. Their diet may include ants, beetles, and various small prey they can find in or near the water.",
    "In the wild, Fire-bellied toads typically have a lifespan of up to 10 to 15 years, depending on environmental conditions and predation.",
    "Fire-bellied toads are known for their colorful ventral (belly) skin, which typically features bright red or orange coloration. This serves as a warning to potential predators that they are toxic. They produce toxins through their skin glands, which can be irritating or even toxic to predators that attempt to consume them. While not extremely toxic to humans, it's essential to handle them with care.",
    "Fire-bellied toads are named for their strikingly colorful belly patterns, which they display as a warning signal to potential predators. These toads are well adapted to both terrestrial and aquatic environments, often found near water bodies. They are known for their unique behavior of arching their bodies and displaying their bright, contrasting colors when they feel threatened. Some species within the Bombina genus are popular as pets in the exotic pet trade, thanks to their vibrant coloration and relatively small size.",
)

addFrogSpecies(
    "Panamanian Golden Frog (Atelopus zeteki)",
    "Adult Panamanian Golden Frogs are relatively small, with sizes typically ranging from 1.2 to 2.4 inches (3 to 6 centimeters) in length. They have a robust build with vibrant yellow or golden skin.",
    "These frogs are endemic to the high-altitude cloud forests and montane forests of western-central Panama. They inhabit mossy and humid montane forests near fast-flowing streams and rivers.",
    "Natural predators of Panamanian Golden Frogs include various snakes, birds, and larger amphibians. However, one of the primary reasons for their critically endangered status is a devastating pathogenic fungus known as chytridiomycosis, which has had a catastrophic impact on their populations.",
    "Panamanian Golden Frogs are insectivorous and primarily feed on a diet of small invertebrates, including insects and other arthropods found in their forested habitats.",
    "The lifespan of these frogs in the wild is not extensively documented but is estimated to be several years, typically up to five years or more, depending on environmental conditions and predation.",
    "Panamanian Golden Frogs are highly toxic. They are known for their potent skin toxins, which they use as a defense mechanism against predators. These toxins can be harmful or even deadly to animals that attempt to consume them. Their bright coloration serves as a warning signal to potential predators, indicating their toxicity.",
    "Panamanian Golden Frogs are culturally significant in Panama and are considered a national symbol and good luck charm. Their vibrant golden coloration makes them visually striking and easily recognizable. Males are known for their distinctive and melodious calls, which they use to communicate with potential mates. Chytridiomycosis, a fungal disease affecting amphibians worldwide, has had a devastating impact on Panamanian Golden Frogs, and they are currently critically endangered in the wild.",
)

addFrogSpecies(
    "Green Tree Frog (Hyla cinerea)",
    "Green Tree Frogs are relatively small, with sizes typically ranging from 1.5 to 2.5 inches (3.8 to 6.3 centimeters) in length. They have a slender build with bright green skin, although their coloration can vary.",
    "These frogs are found in a variety of habitats, including swamps, marshes, forests, and urban areas, throughout the southeastern United States. They are often associated with wetlands and are excellent climbers, typically residing in trees and shrubs.",
    "Natural predators of Green Tree Frogs include various birds, snakes, larger amphibians, and small mammals. They may also be preyed upon by certain invertebrates.",
    "Green Tree Frogs are insectivorous and primarily feed on a diet of insects, spiders, and other small invertebrates. They are known for their ability to capture prey with their long, sticky tongues.",
    "In the wild, Green Tree Frogs typically have a lifespan of 5 to 10 years, depending on factors such as environmental conditions and predation.",
    "Green Tree Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
    "Green Tree Frogs are known for their vibrant green coloration, which serves as camouflage in their leafy habitats. They are excellent climbers and can often be found clinging to vegetation near water sources. These frogs are often heard at night, producing a distinctive and pleasant-sounding call, which can vary by region. Green Tree Frogs are adaptable and can thrive in various environments, including urban areas with suitable habitats.",
)

addFrogSpecies(
    "Golden Poison Dart Frog (Phyllobates terribilis)",
    "The Golden Poison Dart Frog is a relatively small frog, typically ranging from about 1.2 to 2.4 inches (3 to 6 centimeters) in length.",
    "These frogs are native to the rainforests of western Colombia in South America. They inhabit the leaf litter on the forest floor and are often found in humid, tropical rainforest environments.",
    "Despite their small size, these frogs are extremely toxic and have very few natural predators in their native habitat. They are largely avoided by most animals. However, some snakes are known to be resistant to their toxins and may prey on them.",
    "The diet of the Golden Poison Dart Frog primarily consists of ants and termites. These frogs feed on a wide variety of small arthropods, and their diet plays a role in the development of their toxic skin secretions.",
    "In captivity, Golden Poison Dart Frogs can live up to 10 to 15 years. However, their lifespan in the wild may vary and is influenced by various factors.",
    "The Golden Poison Dart Frog is one of the most toxic animals on Earth. Its skin contains potent neurotoxins known as batrachotoxins, which are extremely toxic and can be deadly if ingested. Indigenous people have used the toxic secretions from these frogs to poison the tips of blowdarts for hunting, hence their name.",
    "The vibrant colors of the Golden Poison Dart Frog serve as a warning to potential predators that they are toxic. These frogs are aposematic, meaning they use bright coloration to signal their toxicity. The toxicity of these frogs is thought to be linked to their diet. In captivity, where they are not exposed to the same diet as in the wild, they do not develop the same level of toxicity. There are some local indigenous communities that have used the toxins from these frogs for centuries to poison their blowgun darts for hunting.",
)

addFrogSpecies(
    "African Clawed Frog (Xenopus laevis)",
    "Adult African Clawed Frogs can reach a length of about 3 to 5.5 inches (7.5 to 14 centimeters). They have a streamlined, aquatic body.",
    "These frogs are native to various freshwater habitats in sub-Saharan Africa. They can be found in rivers, ponds, lakes, and other still or slow-moving bodies of water. They are adaptable and can live in a range of aquatic environments.",
    "While African Clawed Frogs may face predation from aquatic invertebrates and large fish, they are often not preferred prey due to their smooth, toxic skin. However, they are more vulnerable during their tadpole and egg stages.",
    "African Clawed Frogs are carnivorous and primarily feed on small aquatic invertebrates. Their diet includes insects, crustaceans, small fish, and other aquatic organisms. They are skilled hunters and use their webbed feet to catch prey.",
    "In the wild, African Clawed Frogs typically live for 5 to 15 years, but in captivity, they can live even longer with proper care.",
    "African Clawed Frogs are not considered poisonous or toxic like some other frog species. They lack the potent skin toxins found in many amphibians. However, their skin secretions can be irritating to human skin and mucous membranes, so it's essential to handle them with care.",
    "These frogs are known for their distinctive appearance, including webbed feet and small claws, which give them their name. African Clawed Frogs have been widely used in scientific research, especially in the fields of developmental biology and genetics. They are one of the few amphibian species that do not undergo a true metamorphosis; instead, they retain their aquatic, tadpole-like characteristics throughout their lives.",
)

addFrogSpecies(
    "Glass Frog (Centrolenidae family)",
    "The size of Glass Frogs varies depending on the species. They typically range from around 1 to 3 inches (2.5 to 7.5 centimeters) in length.",
    "Glass Frogs are primarily found in the rainforests and cloud forests of Central and South America, particularly in countries like Costa Rica, Panama, Colombia, Ecuador, and others. They are arboreal, which means they spend much of their time in the trees and vegetation near streams and rivers.",
    "Predators of Glass Frogs can include various birds, snakes, larger amphibians, and some mammals. Their semi-transparent skin can make them vulnerable to visual predators, but their green coloration helps with camouflage.",
    "Glass Frogs are insectivorous, primarily feeding on a diet of insects and other small invertebrates found in their rainforest habitat.",
    "The lifespan of Glass Frogs in the wild varies by species but is estimated to be several years, typically up to 5 years or more, depending on environmental conditions and predation.",
    "While many species of frogs are known for their skin toxins, Glass Frogs are generally not considered highly poisonous or toxic. They lack the potent skin toxins found in some other frog families.",
    "The primary distinguishing feature of Glass Frogs is their translucent skin, which allows you to see their internal organs, including the heart, liver, and gastrointestinal tract. These frogs are known for their unique breeding behavior. Males often guard and protect their eggs, which they attach to the undersides of leaves hanging over streams. This protects the eggs from aquatic predators.",
)

addFrogSpecies(
    "Tomato Frog (Dyscophus species)",
    "Tomato Frogs are relatively small to medium-sized frogs, typically ranging from about 2 to 4 inches (5 to 10 centimeters) in length, depending on the species and age.",
    "Tomato Frogs are native to Madagascar, an island nation off the southeastern coast of Africa. They inhabit various environments on the island, including rainforests, swamps, and wetlands. They are often associated with shallow, slow-moving bodies of water.",
    "Predators of Tomato Frogs can include various birds, snakes, larger amphibians, and some mammals. Their bright coloration serves as a warning to potential predators that they may be toxic, deterring them from attempting to consume the frogs.",
    "Tomato Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates found in their wetland and forest habitats. They may consume ants, termites, and other small arthropods.",
    "The lifespan of Tomato Frogs in the wild is not extensively documented but is estimated to be several years, typically up to 5 years or more.",
    "Tomato Frogs are known for their skin toxins, which can be harmful to potential predators. The bright red or orange coloration is an aposematic warning to predators, signaling their toxicity. When threatened, they can secrete a milky substance from their skin that contains toxins, causing irritation or harm to potential predators.",
    "Tomato Frogs are named for their vibrant red or orange coloration, which resembles a ripe tomato. This bright color serves as a warning to predators that they are toxic, and their skin secretions can be harmful. They have a robust and heavy build compared to some other frogs, which contributes to their distinctive appearance. Tomato Frogs are known for their explosive breeding behavior, which often occurs after heavy rainfall. Males call loudly to attract females, and they lay their eggs in temporary pools of water where tadpoles develop.",
)

addFrogSpecies(
    "Goliath Frog (Conraua goliath)",
    "The Goliath Frog is one of the largest frog species in the world. Adult Goliath Frogs can reach a length of up to 12.6 inches (32 centimeters) and weigh up to 3.3 kilograms (7.3 pounds). Tadpoles of this species can also grow to substantial sizes.",
    "Goliath Frogs are native to the rainforests of Central and West Africa, specifically found in the regions of Equatorial Guinea and Cameroon. They inhabit fast-flowing rivers and streams within the dense rainforest, preferring areas with rocky substrates.",
    "Despite their impressive size, Goliath Frogs have some natural predators. Their primary predators include large water birds, such as herons, and various aquatic predators. Additionally, humans pose a threat due to habitat destruction and over-harvesting.",
    "Goliath Frogs are opportunistic carnivores, primarily feeding on a diet of insects, small vertebrates, and invertebrates that they can capture near the water's edge. They are known to consume a variety of prey, including insects, crabs, and small fish.",
    "The exact lifespan of Goliath Frogs in the wild is not well-documented, but they are believed to live several years. In captivity, they may live longer, potentially up to 15 years.",
    "Goliath Frogs are not known to be poisonous or toxic in the same way some other frog species are. They rely more on their size and camouflage for protection.",
    "Goliath Frogs are the world's largest frogs, both in terms of size and weight. Their massive appearance and size distinguish them from most other frog species. They have a remarkable and unique breeding behavior, where the male frogs call loudly to attract females. The female Goliath Frogs lay their eggs in or near fast-flowing rivers, and the male guards the eggs and tadpoles until they metamorphose into froglets. The large size of Goliath Frogs is thought to be an adaptation to the fast-flowing streams they inhabit. Their size helps them withstand the strong currents and maintain their position within the water. Goliath Frogs have a greenish-brown coloration with mottled patterns on their skin, which provides excellent camouflage in their lush rainforest environment.",
)

addFrogSpecies(
    "Wood Frog (Rana sylvatica)",
    "Wood Frogs are small to medium-sized amphibians, typically ranging from about 2 to 2.75 inches (5 to 7 centimeters) in length.",
    "Wood Frogs are found in various parts of North America, primarily in regions with temperate and subarctic climates. They inhabit a range of environments, including forests, bogs, and wetlands. These frogs are known for their adaptability and ability to thrive in cold and forested areas.",
    "Wood Frogs have a variety of predators, including snakes, birds, larger amphibians, and small mammals. These frogs are also preyed upon by certain invertebrates. Due to their cryptic coloration, they can often evade predation by blending into their forested surroundings.",
    "Wood Frogs are insectivorous and primarily feed on a diet of insects and other small invertebrates. They are known to consume prey such as ants, beetles, and other arthropods.",
    "In the wild, Wood Frogs typically have a lifespan of 2 to 3 years, although some individuals may live longer under favorable conditions.",
    "Wood Frogs are not known to be highly poisonous or toxic. They lack the potent skin toxins found in some other frog species.",
    "Wood Frogs are well adapted to their cold habitats and can endure freezing temperatures during hibernation. They enter a state of hibernation in the winter months, where their bodies can freeze and then thaw when they awaken in the spring. These frogs have a relatively wide distribution range across North America, and they are often found in forested areas with access to suitable breeding sites. The ability of Wood Frogs to tolerate freezing temperatures is due to the production of a cryoprotectant substance that prevents ice formation within their cells. This adaptation allows them to survive in cold climates.",
)

addFrogSpecies(
    "Poison Dart Frog (Dendrobatidae family)",
    "The size of Poison Dart Frogs varies depending on the species. They can range from as small as 0.5 inches (1.3 centimeters) to about 2.4 inches (6 centimeters) in length.",
    "Poison Dart Frogs are primarily found in Central and South America, inhabiting various rainforests, tropical forests, and other humid and lush environments. Their distribution varies based on the specific species.",
    "Predators of Poison Dart Frogs can include certain snakes, birds, and larger amphibians. However, not all species in the family are toxic, and some non-toxic species lack potent skin toxins. The toxicity of Poison Dart Frogs is generally associated with their diet in the wild.",
    "Poison Dart Frogs are insectivorous and primarily feed on a diet consisting of small invertebrates. They are known to consume a variety of prey, including ants, termites, beetles, and other small arthropods.",
    "The lifespan of Poison Dart Frogs can vary by species but is typically several years in the wild. In captivity, they can live longer under suitable conditions.",
    "Many species of Poison Dart Frogs are highly toxic, and their skin secretes potent toxins. These toxins are used as a defense mechanism to deter potential predators. Indigenous peoples in their native regions have used these toxins to poison the tips of blowdarts for hunting, hence the name 'dart frog.' The level of toxicity can vary among species, and not all members of the family are toxic. Captive-bred Poison Dart Frogs often lack the same level of toxicity as their wild counterparts because their diet in captivity is different.",
    "Some species of Poison Dart Frogs exhibit vibrant and striking coloration, which is thought to be a warning to potential predators about their toxicity. The toxins of Poison Dart Frogs are believed to come from their diet in the wild, particularly ants and other small arthropods. In captivity, when they are not exposed to the same diet, they may lose their toxicity. Poison Dart Frogs are known for their complex social behaviors and vocalizations, which are used for communication and territorial purposes.",
)

addFrogSpecies(
    "Red-eyed Tree Frog (Agalychnis callidryas)",
    "Red-eyed Tree Frogs are relatively small, typically ranging from about 2 to 2.5 inches (5 to 7 centimeters) in length.",
    "These tree frogs are primarily found in the lowland rainforests and tropical jungles of Central America, including countries like Mexico, Costa Rica, Nicaragua, and Honduras. They are arboreal and spend most of their lives in the trees.",
    "The primary predators of Red-eyed Tree Frogs include various birds, snakes, and larger amphibians. These frogs rely on their vibrant coloration and unique markings as a form of aposematism, which is a warning signal to potential predators.",
    "Red-eyed Tree Frogs are insectivores and primarily feed on a diet of small invertebrates, such as crickets, flies, moths, and other small arthropods.",
    "In the wild, Red-eyed Tree Frogs typically have a lifespan of about 5 years. However, they may live longer in captivity under suitable conditions.",
    "Red-eyed Tree Frogs are not considered highly poisonous or toxic like some other frog species. Their skin does secrete a mild toxin, but it is generally not dangerous to humans. Their bright colors are more of a warning to predators that they are not safe to eat.",
    "Red-eyed Tree Frogs are known for their striking and vibrant appearance, with their bright green bodies, blue flanks, orange toes, and, of course, their large, bright red eyes. They have specialized toe pads that help them cling to leaves and branches in the trees. These toe pads are lined with tiny adhesive disks. Red-eyed Tree Frogs are nocturnal, meaning they are most active at night. During the day, they rest on leaves with their eyes closed to conserve energy and hide from potential predators. Mating rituals of Red-eyed Tree Frogs are quite interesting, involving calling to attract mates, amplexus (the mating embrace), and the male fertilizing the eggs as the female lays them on leaves overhanging water.",
)

addFrogSpecies(
    "American Bullfrog (Lithobates catesbeianus)",
    "American Bullfrogs are one of the largest frog species and can reach lengths of up to 6 to 8 inches (15 to 20 centimeters) or even larger.",
    "These frogs are native to North America and are found in a wide range of aquatic habitats, including ponds, lakes, slow-moving rivers, and marshes. They are highly adaptable and can thrive in both natural and man-made water bodies.",
    "While American Bullfrogs are large and less vulnerable to predation as adults, their tadpoles and young frogs are susceptible to predation by a variety of aquatic animals, including fish, birds, snakes, and even other bullfrogs.",
    "Bullfrogs are voracious predators and eat a wide range of prey, including insects, other smaller frogs, fish, small mammals, and even birds. They are known for their powerful jaws and the ability to consume prey items nearly as large as themselves.",
    "In the wild, American Bullfrogs can live for several years, typically around 7 to 9 years. Their lifespan may vary depending on factors like habitat quality and predation.",
    "American Bullfrogs are not considered poisonous or toxic to humans. However, they do have a set of powerful jaws and sharp teeth, so handling them can result in a painful bite. It's also worth noting that the skin of amphibians like the American Bullfrog can secrete toxins, but these are not typically harmful to humans.",
    "The American Bullfrog is known for its distinctive 'jug-o'-rum' call, which is a loud, resonant, and repetitive sound produced by the males during the breeding season. They have a unique and characteristic olive-green coloration with a light-colored belly. American Bullfrogs are considered invasive species in some regions where they have been introduced. Their large size and voracious appetite can have negative impacts on local ecosystems, especially when they outcompete native species. Bullfrogs are powerful swimmers and are capable of leaping great distances when attempting to escape predators.",
)

addFrogSpecies(
    "Purple Frog (Nasikabatrachus sahyadrensis)",
    "Purple Frogs are relatively large and robust frogs. They typically grow to about 2.0 to 2.5 inches (5 to 6.3 centimeters) in length.",
    "These frogs are endemic to the Western Ghats in India, specifically in the states of Kerala and Karnataka. They are primarily found in the Western Ghats' high-altitude regions, which are montane grasslands and shola forests.",
    "As adult frogs, they have limited natural predators due to their underground and burrowing lifestyle. However, they may face threats from certain ground-dwelling animals like snakes and small mammals. Their underground lifestyle keeps them well-hidden.",
    "Purple Frogs are burrowing frogs and primarily feed on subterranean prey like termites and ants. Their specialized diet is well-suited for their underground lifestyle.",
    "The lifespan of Purple Frogs in the wild is not well-documented, but they likely have a relatively long lifespan, possibly several years.",
    "Purple Frogs are not known to be poisonous or toxic. Their adaptation to burrowing and the underground environment makes them less exposed to potential predators. Their skin is not known to secrete toxins.",
    "Purple Frogs are known for their unique and peculiar appearance. They have a stout, bloated body with a purplish-brown coloration. They have a wrinkled and tubular body shape, which is an adaptation for their burrowing lifestyle. These frogs are fossorial, meaning they spend most of their lives underground. They emerge briefly during the monsoon season to breed. Purple Frogs are famous for their unusual and loud calls, which are often described as 'mooing' sounds. These vocalizations play a significant role in their breeding behavior. They are an ancient and primitive frog species, and their lineage is estimated to be over 100 million years old.",
)

@app.route('/posts', methods=["GET"])
def post():
    return jsonify(frog_species_list)
    
@app.before_first_request
def activate_job():  # activate these items 
    initJokes()
    initUsers()
    initPlayers()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8014")
