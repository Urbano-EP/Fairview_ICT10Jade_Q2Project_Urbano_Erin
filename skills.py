from pyscript import document, display

def show_element(e):
    document.getElementById("output1").innerHTML = ""
    
    elements = {
    "h": ["Hydrogen", 1, 1.008],
    "he": ["Helium", 2, 4.0026],
    "c": ["Carbon", 6, 12.011],
    "n": ["Nitrogen", 7, 14.007],
    "o": ["Oxygen", 8, 15.999],
    "f": ["Fluorine", 9, 18.998],
    "ne": ["Neon", 10, 20.180],
    "p": ["Phosphorus", 15, 30.974],
    "s": ["Sulfur", 16, 32.06],
    "cl": ["Chlorine", 17, 35.45],
    "ar": ["Argon", 18, 39.948],
    "se": ["Selenium", 34, 78.971],
    "br": ["Bromine", 35, 79.904],
    "kr": ["Krypton", 36, 83.798],
    "i": ["Iodine", 53, 126.904],
    "xe": ["Xenon", 54, 131.293],
    "rn": ["Radon", 86, 222]
}
    element_symbol = document.getElementById('element').value

    element_info = elements.get(element_symbol, ["Element Not Found", "Unknown", "Unknown"])

    document.getElementById("output1").innerHTML = f"""
        Symbol: {element_symbol.upper()}<br>
        Element: {elements.get(element_symbol, ["Unknown"])[0]}<br>
        Atomic Number: {elements.get(element_symbol, ["Unknown", "Unknown"])[1]}<br>
        Atomic Mass: {elements.get(element_symbol, ["Unknown", "Unknown", "Unknown"])[2]}<br>
        """
