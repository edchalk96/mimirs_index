# Testing

[Return to Mimir's Index README.md](./README.md)

## Manual Testing

Manual testing was selected over automated testing for this project because it offered a more efficient balance between time investment and overall outcome. Given the project's current scope, verifying functionality manually proved to be significantly faster than writing and maintaining automated test suites. However, automated testing is planned for implementation during the next development phase to support future scalability as new features and data are added.

### base.html | Header and Footer

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Logo navigation link to to home page (index.html) upon clicking | User redirected to index.html | Working |
| Navbar "Home" navigation to index.html | User redirected to index.html | Working |
| Navbar "The Edda Library" navigation to the_edda_library.html | User redirected to the_edda_library.html | Working |
| Navbar "The Entity Archive" navigation to the_entity_archive.html | User redirected to the_entity_archive.html | Working |
| Navbar "The Forge" navigation to the_forge.html | User redirected to the_forge.html | Working |
| Log In navigation within nav bar to login.html | User redirected to login.html | Working |
| Register navigation within nav bar to signup.html | User redirected to signup.html | Working |
| Logged in user - Log out navigation within nav bar to logout.html | User redirected to logout.html | Working |
| Admin user - Navigation to djangos admin page | User redirected to the django admin page | Working |
| Welcome message in navigatin for logged in user | User is presented with personalised welcome message in nav bar | Working |
| Contact Developer link to modal | Modal pop up to contact developer | Working |
| Successfully send a message to developer after submitting | Email sent to developer with users message | Working (antivirus shield turned off) |
| Navigation to developer github page | User is redrected to the developers github page | Working |
| Navigation to developers discord profile | User is redrected to the developers discord profile | Working |

### Account pages | Login, Logout, Register

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| User able to input email or username and password and log in | User is successfully logged in to site | Working |
| User able to select "Forgot your password" to change password | User redirected to allauths change password page | Working |
| User able to select Remember Me to stay logged in on net visit | User is succesfully remembered and logged in upon next visit | Working |
| Redirect user to register in login page | User can click on REGISTER HERE to be taken to signup page | Working |
| User able to input a username, email and password and create an acoount | User can successfully create an account to the site | Working |
| User can redirect to login page if they already have an account | "ENTER THE HALLS HERE" redirects user to the login page | Working |
| User can select to logout of the site | User can succesfully logout of the site | Working |

### index.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Nav card "The Edda Library" navigation to the_edda_library.html | User redirected to the_edda_library.html | Working |
| Nav card "The Entity Archive" navigation to the_entity_archive.html | User redirected to the_entity_archive.html | Working |
| Nav card "The Forge" navigation to the_forge.html | User redirected to the_forge.html | Working |
| Random lore entry in the home page | A random lore entry from the database is generated in the home page | Working |
| User can view the random lore entry | "Open the scroll" link redirects user to specfic lore entry being shown | Working |
| User can view the mentioned/linked entities in the random lore | Use is redirected to relevant entity profile | Working |

### the_edda_library.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Paginated list of all lore entries is generated | User is presented with a paginated list of all published lore entries in the database | Working |
| Paginated list can be sorted | Sort function succeessfuully sorts list on A-Z, Z-A, Newest and Oldest | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succcesfully navigates user in the paginated list | Working |
| Redirection to specific lore entry page | Clicking on a lore enry card redirects user to specific lore entry page | Working |