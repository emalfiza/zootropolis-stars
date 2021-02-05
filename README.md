## Zootropolis Stars
---


### Milestone Project - Full Stack Frameworks with Django
---
Zootropolis stars is an e-commerce website aimed at fans of the amazing super hot Zootopia characters. Through it, the fans can purchase goods that replicate items that exist whithin the world of Disney, Zootopia movies and games like Zootopia Crime Files.

The Zootopia copyrights is held by Disney. No copyrights infringement is intended with this ecommerce website, it's created for educational purposes only, and no money is being made through the Zootrolopis Stars website.

The project utalizes Python 3, Django 3.0.7, JavaScript and various other Frameworks and libraries. Full CRUD functionality is offered throughout features of the project.


### Project Purpose
---
Zootopia is defiantly one of those amazing Disney movies that I could easily rewatch over and over again. 

The underlying mystery of these animals becoming like animals is an interesting concept to see from their perspective. 

Fans of Zootopia like myself wildy wants to collect and archive the super hot characters merchs. If you looking to have new collectives your on the right place. Vamos...


#### [See here for a deployed app](https://zootropolis-stars.herokuapp.com/)

#### [See here for the high fidelity wireframe](https://c79emn.axshare.com/)
---
High fidelity prototype is created in Axure, as this helped me design better.


### Quick Quide**
---
###### HOME
The home page features a very special hero image of the Zootopia Stars and a nice bootstrap jumotron rgba opacity background colour with a large SHOP NOW button.

<details>
<summary>See here for the Home Page</summary>

<p align="center">
    <img height="350" src="./images/home-page.png" alt="home page">
</p>
</details>


###### ALL PRODUCTS
The all products page is a filtered products which is exist on the site. This can be accessed by clicking the ALL PRODUCTS label on the navigation bar and as well as the SHOP NOW button on the home page.

<details>
<summary>See here for the All Product Page</summary>

<p align="center">
    <img height="350" src="./images/all-product.png" alt="all-product page">
</p>
</details>


###### CLOTHING
The clothing label filters only the clothing products which exist in the database. This can be accessed by clicking on the clothing label on the navigation bar.

<details>
<summary>See here for the Clothing Page</summary>

<p align="center">
    <img height="350" src="./images/clothing-page.png" alt="clothing page">
</p>
</details>


###### CANVAS
The canvas label filters only the canvas and prints products of the Zootopia which exist in the database. This can be accessed by clicking on the canvas label on the navigation bar. 

<details>
<summary>See here for the Canvas Page</summary>

<p align="center">
    <img height="350" src="./images/canvas-page.png" alt="canvas prints page">
</p>
</details>


###### SPECIAL OFFER
The special offer label filters only the products which are on special offer that can be only added by the superuser on the admin page. This can be accessed by clicking on the special offer label on the navigation bar.

<details>
<summary>See here for the Special Offer Page</summary>

<p align="center">
    <img height="350" src="./images/special-offer.png" alt="special offer page">
</p>
</details>


***NOTE***:
There is a scroll-to-top button which lives on the right buttom cornor of the below pages:
 - ALL PRODUCTS
 - CLOTHING
 - CANVAS
 - SPECIAL OFFER

The scroll-to-top-button gives the user the ability to get back to the top of the page if there is too many lines of products.


###### PRODUCTS DETAIL
Clinking on the product image will take the user to the product detail page. The product detail page contains the product picture with a description below the picture. The name, price, category, quantity, add to bag and back to shopping on the right of the product picture on the large screen. It will adjust and response defferently on the small screen size.

<details>
<summary>See here for the Product Detail Page</summary>

<p align="center">
    <img height="350" src="./images/product-detail.png" alt="product-detail page">
</p>
</details>


###### SHOPPING BAG
The shopping bag consist of the product picture on the left, name of the product, price, quantity and subtotal filling there places horozintally. The quantity allows the user to update and remove the item from the shopping bag by clicking the update and remove link. On the buttom right cornor of the page is the bag total, delivery cost, grand total, keep shopping bag button and secure checkout button.

<details>
<summary>See here for the Shopping Bag Page</summary>

<p align="center">
    <img height="350" src="./images/shopping-bag.png" alt="shopping bag page">
</p>
</details>


###### CHECKOUT
The checkout page is accessable by clicking the secure checkout button from the shopping bag. The checkout page is consist of the order summary at the top of the page. The delivery and stripe payment form fields are splited into two columns. The delivery form fields on the left and the payment form on the right along with adjust bag button and complete order button. In order to test the checkout functionality, the user can fill the delivery form and the stripe payment with the following stripe test numbers:

4242 4242 4242 4242 04/24 242 42424

<details>
<summary>See here for the Checkout</summary>

<p align="center">
    <img height="350" src="./images/checkout.png" alt="checkout page">
</p>
</details>


###### CHECKOUT SUCCESS
Clicking the complete order button on the checkout page will take the user to the checkout success page only all the details are correct. The checkout success page is a simple thank you message and a shop more button that gives the user the ability to go back to the product page.

<details>
<summary>See here for the Checkout Success Page</summary>

<p align="center">
    <img height="350" src="./images/checkout-successpng" alt="checkout success page">
</p>
</details>


###### My Account
My Account gives the user the ease to register, login and logout with simple layout of the django all auth template.

<details>
<summary>See here for the Account Page</summary>

<p align="center">
    <img height="350" src="./images/account.png" alt="account page">
</p>
</details>


### UX
---
#### User stories
The UX has been designed with the end-user in mind and as expectations in terms of front-end design are ever increasing, I opted to utilise Bootstrap and take the inspiration from the Code Institute Django Project, which I found very beautiful for my design and responsive layout.

#### Ideal Client
- English speaking.
- Young people

#### All visitors to the site will expect/want/need:
- As a new user will be eager to find the content of Zootopia characters.
- As a new user to this store, I want to view the new items of Zootopia.
- As a new user, I want to navigate easily.
- The images and text content to be helpful, understandable and bring about a positive response or interesting experience.
- To easily find what the user is looking for. Want the layout of the site to make sense so the user is not confused, frustrated or bored using it.
- The information I am presented with to be laid out in a way that is easy for the user to navigate, so that the user can find what they need quickly and efficiently then return to the home page immediately.
- As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices. 


### Features
---
Each page features a responsive ***navigation bar*** with a rabbit ear logo (top left) only appears on bigger screen size and unhides on small screen size to make the navigation simple and clean. 

The website products labeling is placed right at the middle of the ***navigation bar*** on the bigger screen size and shrink into the humberger bootstrap menue on the small screen size.

On the right side of the ***navigation bar*** live the site user profile and the shopping basket on the large screen size and adjust chronoligically by size on the middle and left of the navigation on the small screen size.

The home page features a hero image of Zootopia Stars, Officer Judy (The Rabbit) and Nick Wilde (The Fox) and the purpose of the hero image on the website is to attract the attention and give a positive emotional response to the user, this was proven to me, when I had the 2nd mentoring session with my mentor ***Brian Macharia***. He was guiding me to the steps of completing the project and as soon as, he came across the hero image for a moment he was bewildered by the hero image.


#### Existing Features
- Header Navigation Bar or navigation system - Exist on every page and it aid vistors to navigate easily and find what they are looking for swiftly.
- Header Logo - Exist on every page and it allows the users to recognize the business brand. Clicking the logo from any where on the site will take the user back to the home page.
- My Account - Exist on every page and it gives the user the ability to update his/her account information.
- Shopping Bag - Exist on every page and keeps the user item in a coockie session and gives the user the ability to update and checkout for the product.
- All Products Label - Exist on every page and it allows the user to filter all the products live in the database.
- Clothing Label - Exist on every page and it allows the user to filter only the zootropolis clothing products.
- Canvas Label - Exist on every page and it allows the user to filter only the zootropolis printing and arts.
- Special Offer Label - exist on every page and it allows the user to filter only the zootropolis products which are on offer.
- Home Page Hero Image - exist only on the home page where the users first land. It connect the user to the site to explore more.


#### Future Developments
- Generating order number functionality.
- Adding the functionlity, the user can check order history.
- Bootstrap toasts for pop up messages.


### The Structure plan
---
Considering what would be logical and reasonable e-commerce store project is about usibility and functionlity more than being fancy and decorated, That is why I kept the simple black and white feeling and considering intuitive IA (Information Architecture), the structure has been kept as simplistic as possible on App.

Information architecture is just a small part of the User Experience but imperative to achieve the functionality without either users or user/contributors losing interest and leaving the site which would be no winning margin to the business purpose.


### Defensive design planning.
---
Defensive design planning for this project at this moment of the development was not required as this app was planned for a educational purpose and can be developed at any time.


### Technologies Used
---
1. [HTML5](https://en.wikipedia.org/wiki/HTML5) - Semantic markup language as the shell of the site.
2. [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This was used to style the elements of the HTML code.
3. [BOOTSTRAP](https://getbootstrap.com/) - HTML forms, icons, templates with nav bar, buttons and footer.
4. [PYTHON3](https://www.python.org/download/releases/3.0/).
5. [DJANGO](https://docs.djangoproject.com/en/3..0.7/) - Framework to construct and render pages.
6. [GITPOD](https://www.gitpod.io) - IDE 
7. [HEROKU](https://heroku.com/) - Deployment
8. [GITHUB](https://github.com) - Used for version control 
9. [Typora](https://typora.io/) - Language for Readme.md file.
10. [PIP and Pypi libraries]
11. [JQUERY](https://code.jquery.com/jquery-3.3.1.slim.min.js).
12. [JAVASCRIPT] (https://www.javascript.com/).
13. [Am I Responsive?](http://ami.responsivedesign.is/#) - Was used for the responsiveness of the app.
14. [Axure] (https://www.axure.com/) for the high fidelity wireframe



### Testing
---


### Responsive design
---



### Compatibility
---



### Version Control and Heroku Deployment
---




### Credits
---
Thank to the author of the rabbit ears for my logo... copied from the following:

<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>



#### Author
---



#### Inspiration
---



#### Acknowledgements
---


#### Submission
---