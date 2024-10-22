# Ex.06 Restaurant Website
## Date: 22/10/2024

## AIM:
To develop a static Restaurant website to display the food items and services provided by them.

## DESIGN STEPS:

### Step 1:
Requirement collection.

### Step 2:
Creating the layout using HTML and CSS.

### Step 3:
Updating the sample content.

### Step 4:
Choose the appropriate style and color scheme.

### Step 5:
Validate the layout in various browsers.

### Step 6:
Validate the HTML code.

### Step 7:
Publish the website in the given URL.

## PROGRAM:

```
HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Mangata and Gallo</title>
    <meta name= "description" content="A Brief Description">
    <meta name="author" content= "Luxury Jewellery">

    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header section -->
    <header>
        <div class="logo">
            <img src="logo.png" alt="Client Logo">
        </div>
        <nav>
            <ul class="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main content section -->
    <main>
        <!-- Promotional Banner -->
        <section class="promo">
            <h1>Welcome to Little Lemon</h1>
            <p>Have your Favourite taste...</p>
            <img src="img1.png" alt="banner">
            <p>Savor the best of both worlds with our delicious veg and non-veg dishes, crafted to perfection. From mouthwatering starters to irresistible snacks, every bite is a burst of flavor. Join us for a dining experience that satisfies every craving!</p>
        </section>

        <!-- Three columns section -->
        <section class="three-columns">
            <article class="column">
                <h2>Starters and Snacks</h2>
                <img src="img2.png" alt="Starters&Snacks">
                <p>*  Kickstart your cravings with our irresistible starters and snacks, bursting with flavor in every bite.</p>
                <p>*  Perfectly crafted to tease your taste buds, our delicious selection is the ultimate treat for any occasion.</p> 
                <p>*  Indulge in the perfect bite-sized delights!</p>
            </article>
            <article class="column">
                <h2>Vegetarian</h2>
                <img src="img3.png" alt="Veg">
                <p>*  Delight in our fresh, flavorful vegetarian dishes that celebrate nature's finest ingredients.</p>
                <p>*  Each meal is crafted to nourish your body and satisfy your taste buds.</p>
                <p>*  Experience the vibrant taste of wholesome, plant-based goodness!</p>
            </article>
            <article class="column">
                <h2>Non-Vegetarian</h2>
                <img src="img4.png" alt="NonVeg">
                <p>*  Indulge in the rich, savory flavors of our premium non-veg dishes, expertly crafted for true food lovers.</p>
                <p>*  From tender meats to bold spices, every bite promises a taste of perfection.</p>
                <p>*  Satisfy your cravings with our irresistible non-veg delights!</p>
            </article>
        </section>
    </main>

    <!-- Footer section -->
    <footer>
        <div class="footer-left">
            <img src="logo_footer.png" alt="Client Logo">
        </div>
        <div class="footer-right">
            <p>&copy; 2024 Little Lemon. All rights reserved.</p>
        </div>
    </footer>

</body>
</html>
```
```
CSS

/* General reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: 'Times New Roman', Times, serif;
    line-height: 1.6;
}

/* Header section */
header {
    display: block;
    align-items: center;
    padding: 50px 30px;
    background-color: #333;
    color: #fff;
}

.logo img {
    display: block;
    width: 300px;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 40px;
}

nav ul {
    list-style: none;
    text-align: center;
}

nav ul li {
    margin-left: 20px;
    display: inline;
}

nav ul li a {
    text-decoration: none;
    color: #fff;
    padding: 25px 15px;
    transition: background 0.3s;
    font-size: 1.5rem;
}

nav ul li a:hover {
    background-color: #555;
    border-radius: 5px;
}

/* Promo banner */
.promo {
    background-color: #f4f4f4;
    text-align: center;
    padding: 50px 20px;
    margin-bottom: 40px;
}

.promo h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
}

.promo p {
    font-size: 1.5rem;
    color: red;
}

/* Three columns layout */
.three-columns {
    display: flex;
    justify-content: space-around;
    padding: 20px;
}

.column {
    text-align: center;
    flex: 1;
    margin: 0 10px;
}

.column img {
    width: 100%;
    height: auto;
    border-radius: 8px;
}

.column h2 {
    margin: 15px 0;
    color: darkblue;
    font-size: 2.5rem;
}

.column p {
    font-size: 1.5rem;
    color: black;
}

/* Footer styling */
footer {
    background-color: #333;
    color: #fff;
    padding: 20px;
    display: flex;
    justify-content: space-between;
}

.footer-left img {
    width: 400px;
}

.footer-right p {
    margin: 0;
    font-size: 1.5rem;
}

/* Responsive design */
@media (max-width: 768px) {
    .three-columns {
        flex-direction: column;
    }

    .column {
        margin-bottom: 20px;
    }
}
```

## OUTPUT:
![alt text](<REST PRO.jpeg>)

## RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
