# nutrition_database.py
"""
Enhanced nutritional database for food items with allergens and detailed descriptions
All values are per 100g serving
"""


class NutritionDatabase:
    def __init__(self):
        # Nutritional data per 100g with enhanced details
        self.nutrition_data = {
            'sushi': {
                'name': 'Sushi',
                'calories': 150,
                'protein': 7.5,
                'carbs': 28,
                'fat': 1.2,
                'fiber': 1.5,
                'sugar': 5,
                'sodium': 590,
                'description': 'Traditional Japanese dish featuring vinegared rice combined with fresh raw fish, seafood, or vegetables. Sushi is not just a meal but an art form, carefully crafted with precise knife work and balanced flavors.',
                'detailed_description': 'Sushi originated in Japan as a method of preserving fish in fermented rice. Today\'s sushi combines perfectly seasoned sushi rice (shari) with the freshest fish (neta). Common varieties include nigiri (hand-pressed rice topped with fish), maki (rolled sushi), and sashimi (sliced raw fish without rice). The preparation requires years of training to master.',
                'allergens': ['Fish', 'Shellfish (may contain)', 'Soy (soy sauce)', 'Sesame (may contain)'],
                'dietary_info': ['Gluten-Free (without soy sauce)', 'Dairy-Free', 'Low Fat'],
                'health_benefits': ['High in Omega-3 fatty acids', 'Good source of protein', 'Contains beneficial minerals like iodine'],
                'origin': 'Japan',
                'preparation_time': '30-45 minutes',
                'vitamins': {
                    'vitamin_a': '2%',
                    'vitamin_c': '3%',
                    'calcium': '2%',
                    'iron': '8%',
                    'vitamin_b12': '25%',
                    'niacin': '15%'
                }
            },
            'bibimbap': {
                'name': 'Bibimbap',
                'calories': 185,
                'protein': 9.2,
                'carbs': 25,
                'fat': 5.8,
                'fiber': 3.2,
                'sugar': 4.5,
                'sodium': 485,
                'description': 'Korean mixed rice bowl featuring an array of seasoned vegetables, meat, and a fried egg, served with spicy gochujang sauce. A harmonious blend of colors, textures, and flavors in one bowl.',
                'detailed_description': 'Bibimbap, literally meaning "mixed rice," is a signature Korean dish that represents the philosophy of balance in Korean cuisine. The dish typically includes five different colored vegetables (representing the five elements in Korean philosophy), rice, meat (usually beef), and a fried egg on top. Each vegetable is individually seasoned and arranged in separate sections before being mixed together.',
                'allergens': ['Eggs', 'Soy (soy sauce, gochujang)', 'Sesame', 'Gluten (may contain)'],
                'dietary_info': ['High in Fiber', 'Balanced Macronutrients', 'Vegetarian Option Available'],
                'health_benefits': ['Rich in antioxidants from colorful vegetables', 'Good source of complete protein', 'High fiber content aids digestion'],
                'origin': 'Korea',
                'preparation_time': '45-60 minutes',
                'vitamins': {
                    'vitamin_a': '15%',
                    'vitamin_c': '12%',
                    'calcium': '4%',
                    'iron': '12%',
                    'folate': '18%',
                    'vitamin_k': '22%'
                }
            },
            'apple_pie': {
                'name': 'Apple Pie',
                'calories': 265,
                'protein': 2.4,
                'carbs': 38,
                'fat': 12.5,
                'fiber': 2.1,
                'sugar': 18,
                'sodium': 230,
                'description': 'Classic American dessert featuring tender, cinnamon-spiced apples encased in a flaky, buttery pastry crust. Often served warm with vanilla ice cream or whipped cream.',
                'detailed_description': 'Apple pie has been a symbol of American culture since the colonial era. The perfect apple pie balances tart and sweet apples (often Granny Smith and Honeycrisp) with warm spices like cinnamon, nutmeg, and sometimes cardamom. The crust should be golden and flaky, creating a perfect contrast to the soft, caramelized apple filling.',
                'allergens': ['Wheat/Gluten', 'Eggs', 'Dairy (butter)', 'Tree Nuts (may contain)'],
                'dietary_info': ['High in Sugar', 'Contains Refined Carbs', 'Comfort Food'],
                'health_benefits': ['Apples provide fiber and antioxidants', 'Source of vitamin C', 'Contains beneficial plant compounds'],
                'origin': 'United States (popularized)',
                'preparation_time': '90-120 minutes',
                'vitamins': {
                    'vitamin_a': '3%',
                    'vitamin_c': '4%',
                    'calcium': '2%',
                    'iron': '5%',
                    'vitamin_e': '3%',
                    'potassium': '2%'
                }
            },
            'tiramisu': {
                'name': 'Tiramisu',
                'calories': 320,
                'protein': 5.8,
                'carbs': 35,
                'fat': 18,
                'fiber': 0.5,
                'sugar': 22,
                'sodium': 175,
                'description': 'Elegant Italian coffee-flavored dessert made with layers of coffee-soaked ladyfingers and rich mascarpone cream, dusted with cocoa powder. A perfect balance of bitter and sweet.',
                'detailed_description': 'Tiramisu, meaning "pick-me-up" in Italian, is a relatively modern dessert created in the 1960s in the Veneto region. It features delicate savoiardi (ladyfinger cookies) soaked in strong espresso and sometimes liqueur, layered with a luxurious mixture of mascarpone cheese, eggs, and sugar. The final dusting of cocoa powder adds a subtle bitter note that balances the sweetness.',
                'allergens': ['Eggs', 'Dairy (mascarpone, cream)', 'Gluten (ladyfingers)', 'Alcohol (may contain)'],
                'dietary_info': ['High in Fat', 'Contains Raw Eggs', 'Dessert/Treat'],
                'health_benefits': ['Caffeine from coffee', 'Calcium from dairy', 'Energy from carbohydrates'],
                'origin': 'Italy (Veneto region)',
                'preparation_time': '30 minutes + 4 hours chilling',
                'vitamins': {
                    'vitamin_a': '8%',
                    'vitamin_c': '1%',
                    'calcium': '6%',
                    'iron': '3%',
                    'riboflavin': '12%',
                    'phosphorus': '8%'
                }
            },
            'cannoli': {
                'name': 'Cannoli',
                'calories': 340,
                'protein': 6.5,
                'carbs': 34,
                'fat': 20,
                'fiber': 1,
                'sugar': 24,
                'sodium': 190,
                'description': 'Traditional Sicilian pastry featuring crispy fried shells filled with sweet, creamy ricotta filling, often studded with chocolate chips or candied fruits and dusted with powdered sugar.',
                'detailed_description': 'Cannoli originated in Sicily during Arab rule and has become one of Italy\'s most iconic desserts. The shells are made from a wine-enriched dough that\'s rolled thin and fried until golden and crispy. The traditional filling combines fresh ricotta with powdered sugar, vanilla, and often includes chocolate chips, candied citrus peel, or pistachios. The contrast between the crunchy shell and creamy filling is essential.',
                'allergens': ['Wheat/Gluten', 'Dairy (ricotta)', 'Eggs', 'Tree Nuts (may contain pistachios)'],
                'dietary_info': ['High in Sugar', 'High in Fat', 'Traditional Dessert'],
                'health_benefits': ['Calcium from ricotta', 'Protein from dairy', 'Energy from carbohydrates'],
                'origin': 'Sicily, Italy',
                'preparation_time': '60-90 minutes',
                'vitamins': {
                    'vitamin_a': '6%',
                    'vitamin_c': '2%',
                    'calcium': '8%',
                    'iron': '4%',
                    'riboflavin': '10%',
                    'phosphorus': '12%'
                }
            },
            'edamame': {
                'name': 'Edamame',
                'calories': 122,
                'protein': 11.2,
                'carbs': 9.9,
                'fat': 5.2,
                'fiber': 5.2,
                'sugar': 2.2,
                'sodium': 6,
                'description': 'Young soybeans harvested before ripening, typically boiled in salted water and served as a healthy, protein-rich snack or appetizer. Popular in Japanese cuisine and enjoyed worldwide.',
                'detailed_description': 'Edamame are immature soybeans harvested when they are still green and tender, usually around 80% maturity. They have been cultivated in East Asia for over 2,000 years. The beans are typically boiled in well-salted water for 3-5 minutes until tender, then served warm or at room temperature. They\'re enjoyed by squeezing the beans directly from the pod into the mouth.',
                'allergens': ['Soy'],
                'dietary_info': ['Vegan', 'Gluten-Free', 'High Protein', 'High Fiber', 'Low Sodium'],
                'health_benefits': ['Complete protein source', 'Rich in folate and vitamin K', 'Contains isoflavones', 'High in antioxidants', 'Supports heart health'],
                'origin': 'East Asia (China, Japan)',
                'preparation_time': '5-10 minutes',
                'vitamins': {
                    'vitamin_a': '5%',
                    'vitamin_c': '10%',
                    'calcium': '6%',
                    'iron': '13%',
                    'folate': '78%',
                    'vitamin_k': '21%',
                    'magnesium': '16%'
                }
            },
            'falafel': {
                'name': 'Falafel',
                'calories': 333,
                'protein': 13.3,
                'carbs': 31.8,
                'fat': 17.8,
                'fiber': 9.8,
                'sugar': 3.2,
                'sodium': 585,
                'description': 'Middle Eastern deep-fried balls made from ground chickpeas, herbs, and spices. Crispy on the outside, tender on the inside, often served in pita bread or over salads.',
                'detailed_description': 'Falafel is believed to have originated in Egypt but has become a staple throughout the Middle East and Mediterranean. Made from dried chickpeas soaked overnight, then ground with fresh herbs like parsley and cilantro, along with spices such as cumin, coriander, and garlic. The mixture is formed into balls or patties and deep-fried until golden brown and crispy.',
                'allergens': ['Sesame (tahini sauce often served with)', 'May contain traces of nuts'],
                'dietary_info': ['Vegan', 'Gluten-Free (traditionally)', 'High Protein', 'High Fiber'],
                'health_benefits': ['Plant-based protein', 'Rich in fiber', 'Good source of folate', 'Contains antioxidants', 'May help regulate blood sugar'],
                'origin': 'Middle East (possibly Egypt)',
                'preparation_time': '30 minutes + overnight soaking',
                'vitamins': {
                    'vitamin_a': '2%',
                    'vitamin_c': '3%',
                    'calcium': '5%',
                    'iron': '18%',
                    'folate': '45%',
                    'magnesium': '20%',
                    'manganese': '25%'
                }
            },
            'french_toast': {
                'name': 'French Toast',
                'calories': 220,
                'protein': 7.8,
                'carbs': 28,
                'fat': 8.5,
                'fiber': 1.5,
                'sugar': 8,
                'sodium': 420,
                'description': 'Classic breakfast dish made by soaking bread slices in a mixture of beaten eggs and milk, then pan-frying until golden brown. Often served with maple syrup, fresh fruits, or powdered sugar.',
                'detailed_description': 'French toast, known as "pain perdu" (lost bread) in France, was originally created as a way to use stale bread. The bread is dipped in a custard-like mixture of eggs, milk, and often vanilla and cinnamon, then cooked on a griddle or in a pan until golden and slightly caramelized. The best French toast uses thick-cut bread like brioche or challah.',
                'allergens': ['Wheat/Gluten', 'Eggs', 'Dairy (milk)', 'May contain nuts (if topped)'],
                'dietary_info': ['High in Carbohydrates', 'Contains Cholesterol', 'Breakfast Food'],
                'health_benefits': ['Good source of protein from eggs', 'Provides energy from carbohydrates', 'Contains B vitamins'],
                'origin': 'Ancient Rome (modern version from France)',
                'preparation_time': '15-20 minutes',
                'vitamins': {
                    'vitamin_a': '6%',
                    'vitamin_c': '0%',
                    'calcium': '8%',
                    'iron': '10%',
                    'vitamin_d': '8%',
                    'thiamine': '12%',
                    'riboflavin': '15%'
                }
            },
            'ice_cream': {
                'name': 'Ice Cream',
                'calories': 207,
                'protein': 3.5,
                'carbs': 24,
                'fat': 11,
                'fiber': 0.5,
                'sugar': 21,
                'sodium': 80,
                'description': 'Frozen dessert made from dairy products, sugar, and flavorings. Churned while freezing to create a smooth, creamy texture. Available in countless flavors and enjoyed worldwide.',
                'detailed_description': 'Ice cream has evolved from ancient frozen treats to the sophisticated dessert we know today. Made by churning a custard base (cream, milk, sugar, and often egg yolks) while freezing, which incorporates air and prevents large ice crystals from forming. The result is a smooth, creamy texture that melts pleasantly on the tongue. Premium ice creams have higher fat content and less air incorporation.',
                'allergens': ['Dairy (milk, cream)', 'Eggs (may contain)', 'Tree Nuts (flavor dependent)', 'Soy (may contain as emulsifier)'],
                'dietary_info': ['High in Sugar', 'High in Saturated Fat', 'Frozen Dessert', 'Contains Cholesterol'],
                'health_benefits': ['Source of calcium', 'Provides energy', 'Contains vitamin A', 'May boost mood (comfort food)'],
                'origin': 'Ancient China/Persia (modern form from Italy/France)',
                'preparation_time': '30 minutes + 4+ hours freezing',
                'vitamins': {
                    'vitamin_a': '10%',
                    'vitamin_c': '1%',
                    'calcium': '14%',
                    'iron': '1%',
                    'vitamin_d': '6%',
                    'riboflavin': '8%',
                    'phosphorus': '10%'
                }
            },
            'ramen': {
                'name': 'Ramen',
                'calories': 188,
                'protein': 8.5,
                'carbs': 27,
                'fat': 5.4,
                'fiber': 2.3,
                'sugar': 3.5,
                'sodium': 875,
                'description': 'Japanese noodle soup featuring wheat noodles in a flavorful broth, topped with various ingredients like sliced pork, green onions, and eggs. A comforting and satisfying meal.',
                'detailed_description': 'Ramen evolved from Chinese lamian noodles brought to Japan in the early 20th century. True ramen consists of four main components: the broth (which can be based on pork, chicken, miso, or soy), the tare (seasoning), the noodles, and the toppings. Regional variations include Tonkotsu (rich pork bone broth), Shoyu (soy sauce-based), and Miso ramen. Each bowl is carefully constructed to achieve perfect balance.',
                'allergens': ['Wheat/Gluten', 'Soy', 'Eggs (may contain)', 'Fish (may contain in broth)'],
                'dietary_info': ['High in Sodium', 'Contains Refined Carbs', 'Comfort Food'],
                'health_benefits': ['Provides warmth and comfort', 'Good source of protein', 'Contains B vitamins', 'Hydrating'],
                'origin': 'Japan (adapted from Chinese noodles)',
                'preparation_time': '2-12 hours (broth) + 15 minutes assembly',
                'vitamins': {
                    'vitamin_a': '4%',
                    'vitamin_c': '2%',
                    'calcium': '3%',
                    'iron': '10%',
                    'thiamine': '18%',
                    'niacin': '15%',
                    'folate': '8%'
                }
            }
        }

    def get_nutrition(self, food_name, serving_size=100):
        """
        Get nutritional information for a food item

        Args:
            food_name: Name of the food item
            serving_size: Serving size in grams (default 100g)

        Returns:
            Dictionary with scaled nutritional values
        """
        food_name = food_name.lower().replace(' ', '_')

        if food_name not in self.nutrition_data:
            return None

        base_nutrition = self.nutrition_data[food_name].copy()

        # Calculate scaling factor
        scale = serving_size / 100

        # Scale numerical values
        scaled_nutrition = {
            'name': base_nutrition['name'],
            'serving_size': serving_size,
            'calories': round(base_nutrition['calories'] * scale, 1),
            'protein': round(base_nutrition['protein'] * scale, 1),
            'carbs': round(base_nutrition['carbs'] * scale, 1),
            'fat': round(base_nutrition['fat'] * scale, 1),
            'fiber': round(base_nutrition['fiber'] * scale, 1),
            'sugar': round(base_nutrition['sugar'] * scale, 1),
            'sodium': round(base_nutrition['sodium'] * scale, 1),
            'description': base_nutrition['description'],
            'detailed_description': base_nutrition['detailed_description'],
            'allergens': base_nutrition['allergens'],
            'dietary_info': base_nutrition['dietary_info'],
            'health_benefits': base_nutrition['health_benefits'],
            'origin': base_nutrition['origin'],
            'preparation_time': base_nutrition['preparation_time'],
            'vitamins': base_nutrition['vitamins']  # Daily values remain same
        }

        return scaled_nutrition

    def get_all_foods(self):
        """Get list of all available foods"""
        return list(self.nutrition_data.keys())

    def compare_foods(self, food1, food2, serving_size=100):
        """
        Compare nutritional values of two foods

        Args:
            food1: First food item name
            food2: Second food item name
            serving_size: Serving size for comparison

        Returns:
            Dictionary with comparison data
        """
        nutrition1 = self.get_nutrition(food1, serving_size)
        nutrition2 = self.get_nutrition(food2, serving_size)

        if not nutrition1 or not nutrition2:
            return None

        comparison = {
            'food1': nutrition1,
            'food2': nutrition2,
            'differences': {
                'calories': round(nutrition1['calories'] - nutrition2['calories'], 1),
                'protein': round(nutrition1['protein'] - nutrition2['protein'], 1),
                'carbs': round(nutrition1['carbs'] - nutrition2['carbs'], 1),
                'fat': round(nutrition1['fat'] - nutrition2['fat'], 1),
                'fiber': round(nutrition1['fiber'] - nutrition2['fiber'], 1),
                'sugar': round(nutrition1['sugar'] - nutrition2['sugar'], 1),
                'sodium': round(nutrition1['sodium'] - nutrition2['sodium'], 1)
            }
        }

        return comparison