from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class CaptionGenerator:
    # [Previous CaptionGenerator class remains exactly the same]
    def __init__(self):
        self.categories = {
            "Lifestyle": {
                "templates": [
                    "✨ Living the {adjective} life one day at a time #lifestyle",
            "Embracing {noun} and finding joy in the little things 🌟 #mindfulness",
            "Making every moment {adjective} ✨ #lifestyle",
            "Life is {adjective}, enjoy every moment 🌈 #lifestyle",
            "Savoring the {adjective} side of life 🍃 #livingmybestlife"
                ],
                "hashtags": ["#lifestyle", "#mindfulness", "#blessed", "#livingmybestlife"]
            },
            "Travel": {
                "templates": [
                    "Exploring {place} with a {adjective} heart 🌍 #wanderlust",
                    "Adventures in {place}: {verb}ing through paradise ✈️ #travel",
                    "Lost in {place}, found in {emotion} moments 🗺️ #travelling",
                    "Collecting moments, not things 🌟 {place} #travel",
                    "{verb}ing into the heart of {place} ✈️🌏 #wanderlust",
                    "Chillin’ like a villain.",
                    "Living life in the fast lane.",
                    "Catching flights, not feelings.",
                    "Too glam to give a damn.",
                    "Born to stand out.",
                    "Life’s too short to blend in.",
                    "Make waves, move mountains.",
                    "Just another day in paradise.",
                    "Good times and tan lines.",
                    "Chasing dreams and catching sunsets."

                ],
                "hashtags": ["#travel", "#wanderlust", "#explore", "#adventure"]
            },
            "Motivation": {
                "templates": [
                    "Chase your {noun} with the heart of a warrior 💫 #motivation",
                    "{time} is for {verb}ing towards greatness 🎯 #success",
                    "Building {noun} with purpose and passion 🚀 #goals"
                ],
                "hashtags": ["#motivation", "#success", "#goals", "#dreambig"]
            },
            "Fashion": {
                "templates": [
                    "Styling {adjective} vibes for {time} ✨ #fashion",
                    "When your outfit speaks {emotion} volumes 👗 #style",
                    "Expressing {noun} through fashion 💫 #ootd",
                    "Chasing dreams in heels👠✨",
                    "Capture life’s moment, one selfie at a time 📸💖",
                    "Confidence level: Selfie with no filter 🌟",
                    "Sparkle wherever you go ✨🌸",
                    "Slaying the day with style and grace 💃💅",
                    "Sunshine mixed with a little hurricane ☀️🌪️",
                    "Too glam to give a damn 💁‍♀️💋",
                    "Collecting moments, not things 📸💕",
                    "Embrace the glorious mess that you are 🌼🌈",
                    "Strong women lift each other up 💪👯‍♀️",
                    "Just me, myself, and I! 🤳",
                    "Living my best life one selfie at a time 💁‍♀️",
                    "Ready for the weekend! ☀️",
                    "A selfie a day keeps the worries away 🤳",
                    "Treating myself to some me time 💆‍♀️",
                    "Loving this view, even if it’s just me 🥰",
                    "Taking a break from the world and embracing the moment 💫",
                    "Just me, feeling myself 🙌",
                    "Taking some time to enjoy the little things 💛",
                    "Life is a selfie and I’m just living in it 🤳"

                ],
                "hashtags": ["#fashion", "#style", "#ootd", "#fashionista"]
            }
        }
        
        self.words = {
    "adjective": ["elegant", "graceful", "ethereal", "sophisticated", "luxurious", 
                  "timeless", "enchanting", "refined", "exquisite", "divine", "vibrant 🌟", "serene 🌈"],
    "noun": ["elegance", "grace", "sophistication", "beauty", "inspiration", 
             "artistry", "harmony", "serenity", "luxury", "dreams", "peace ☮️", "magic ✨"],
    "verb": ["flourish", "inspire", "elevate", "embrace", "cultivate", 
             "radiate", "enchant", "create", "discover", "journey", "wander 🚶", "soar 🕊️"],
    "emotion": ["beautifully", "gracefully", "serenely", "joyfully", "peacefully", "freely 🕊️", "boldly 🔥"],
    "place": ["this enchanting destination", "this luxurious escape", "this elegant venue", 
              "this magical corner 🌟", "this sophisticated space ✨", "the edge of the world 🌍"],
    "time": ["this moment", "every elegant day", "each graceful moment", "this beautiful season", 
             "the perfect time", "golden hour 🌅", "now 🌟"]
}

    def generate_caption(self, selected_category=None):
        if selected_category and selected_category in self.categories:
            templates = self.categories[selected_category]["templates"]
        else:
            templates = [template for cat in self.categories.values() for template in cat["templates"]]

        template = random.choice(templates)
        for word_type, words in self.words.items():
            while f"{{{word_type}}}" in template:
                template = template.replace(f"{{{word_type}}}", random.choice(words), 1)
        
        return template

caption_generator = CaptionGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_caption():
    data = request.json
    category = data.get('category', None)
    caption = caption_generator.generate_caption(category)
    return jsonify({"caption": caption})

if __name__ == "__main__":
    app.run(debug=True)
