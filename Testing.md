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
| Paginated list can be sorted | Sort function succeessfully sorts list on A-Z, Z-A, Newest and Oldest | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succcesfully navigates user in the paginated list | Working |
| Redirection to specific lore entry page | Clicking on a lore entry card redirects user to specific lore entry page | Working |

### the_entity_archive.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Paginated list of all entities is generated | User is presented with a paginated list of all published entities in the database | Working |
| Search function for published entities | User is abl to search for specific entities succeessfully | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succcesfully navigates user in the paginated list | Working |
| Redirection to specific entitiy profile | Clicking on a entity card redirects user to specific entity profile | Working |

### lore_detail.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Upon clicking specific lore entry link, relevant lore page can be viewed | Successfully renders a lore specific page when clicking on specfic lore link | Working |
| Ability to update lore entry | "Update the Lore" button pops out modal form to update lore entry and successfully submit for review | Working |
| Ability to suggest lore entry is removed the database | "Remove from the library" button pops out delete confirmation modal which then sends a request for entry to be removed | Working |
| Ability to leave a comment | Comment text area at the bottom of page + "carve your thoughts" button successfuly submits comment for review | Working |
| Ability to update user specific comment | "Edit" button successfully updates the bottom comments section to reflect the comment is being updated | Working |
| Ability to delete user specific comment | "Delete" button pops out delete confirmation modal and successfully deletes comment | Working |
| Ability to reply to a previous comment | "Reply" button reveals text area to reply to specific comment and submitting sends it for review | Working |

### entity_profile.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Upon clicking specific entity link, relevant entity profile can be viewed | Successfully renders an entity specific page when clicking entity link | Working |
| Ability to update entity | "Update the Entity" button pops out modal form to update entity and successfully submit for review | Working |
| Ability to suggest entity is removed the database | "Remove from the library" button pops out delete confirmation modal which then sends a request for entity to be removed | Working |
| View lore entries that this entity is mentioned | "Lore Appeances" section generates a list, if any, lore entries the entity has been mentioned and linked to | Working |
| Ability to navigate to lore entry from "Lore Appearances" section | User is able to be redirected to lore page relevant to entity through "View Full Lore" link | Working |

### the_forge.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Fast navigation to forge a lore entry | Clicking "Forge a Lore Entry" button scrolls user to relevant section on page | Working |
| Fast navigation to forge an entity | Clicking "Forge an Entity" button scrolls user to relevant section on page | Working |
| Ability to submit a lore entry | User is able to submit a new lore entry for review | Working |
| Ability to link entities to new lore entry | User is able to link entities mentioned in new lore entry submission | Working |
| Ability to submit an entity | User is able to submit a new entity for review | Working |
| Ability to attach a relevant image to lore or entity | User is able to attach image to entry/entity | Working |

## User Story Validation

The functionality and outcomes outlined above directly align with the [User Stories](./README.md/#user-stories) established during the strategy plane of this project. Every user story has been successfully addressed through these features, with the exception of those previously mentioned in the [Scope Plane](./README.md/#scope-plane), which are slated for implementation during the next phase of development.

## Validator Testing

### HTML

- [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
  - base.html | [Result](./documentation/images/testing/base-html-test.png)
    - 23/26 hidden messages realted to python specific tags. 2/26 related to duplicated id, due to if-else function. 1 due to no h1 heading which is present in index.html.
  - index.html | [Result](./documentation/images/testing/index-html-test.png)
    - All 11 hidden messages related to lack of head element which is in the base.html.
  - the_edda_library.html | [Result](./documentation/images/testing/the-edda-library-html-test.png)
    - All messages related to python relevant code not recognised by validator.
  - the_entity_archive.html | [Result](./documentation/images/testing/the-entity-archive-html-test.png)
    - All messages related to python relevant code not recognised by validator.
  - lore_detail.html | [Result](./documentation/images/testing/lore-detail-html-test.png)
    - All messages related to python relevant code not recognised by validator and skipped heading levels due to modals.
  - entity_profile.html | [Result](./documentation/images/testing/entity-profile-html-test.png)
    - All messages related to python relevant code not recognised by validator and skipped heading levels due to modals.
  - the_forge.html | [Result](./documentation/images/testing/the-forge-html-test.png)
    - All messages related to python relevant code not recognised by validator.
  - 404.html | [Result](./documentation/images/testing/404-html-test.png)
    - All messages related to python relevant code not recognised by validator.
  - 500.html | [Result](./documentation/images/testing/500-html-test.png)
    - All messages related to python relevant code not recognised by validator.

### CSS

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) | [Result](./documentation/images/testing/css-validation.png)
  - Warnings from this validator are all dynamic nature warnings as well as vendor extension warnings

### JavaScript

- [JSHint](https://jshint.com/) - JavaScript Validator
  - base.js | [Result](./documentation/images/testing/base-js-test.png)
    - Warning related to bootstap element
  - comments.js | [Result](./documentation/images/testing/comments-js-test.png)
    - Warning related to bootstap element and function variable used in html code
  - lore-detail.js | [Result](./documentation/images/testing/lore-detail-js-test.png)
    - Undefined variable warnings occuring due to validator looking at JS file in isolation, mistaking external tools, like jQuery's $, for code errors.

### Python

- [PEP8 Python Validator](https://pep8ci.herokuapp.com/)
  - Home App:
    - urls.py | [Result](./documentation/images/testing/home-app-urls-py-test.png)
    - views.py | [Result](./documentation/images/testing/home-app-views-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
  - Mimir's Index:
    - settings.py | [Result](./documentation/images/testing/settings-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
    - urls.py | [Result](./documentation/images/testing/mimirs-index-urls-py-test.png)
    - wsgi.py | [Result](./documentation/images/testing/mimirs-index-wsgi-py-test.png)
  - The Edda Library App:
    - admin.py | [Result](./documentation/images/testing/the-edda-library-admin-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
    - forms.py | [Result](./documentation/images/testing/the-edda-library-forms-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
    - models.py | [Result](./documentation/images/testing/the-edda-library-models-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
    - urls.py | [Result](./documentation/images/testing/the-edda-library-urls-py-test.png)
    - views.py | [Result](./documentation/images/testing/the-edda-library-views-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
  - The Entity Archive App:
    - admin.py | [Result](./documentation/images/testing/the-entity_archive-admin-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
    - forms.py | [Result](./documentation/images/testing/the-entity_archive-forms-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.
    - models.py | [Result](./documentation/images/testing/the-entity_archive-models-py-test.png)
    - urls.py | [Result](./documentation/images/testing/the-entity_archive-urls-py-test.png)
    - views.py | [Result](./documentation/images/testing/the-entity_archive-views-py-test.png)
  - The Forge App:
    - forms.py | [Result](./documentation/images/testing/the-forge-forms-py-test.png)
    - urls.py | [Result](./documentation/images/testing/the-forge-forms-py-test.png)
    - views.py | [Result](./documentation/images/testing/the-forge-views-py-test.png)
      - E501 error due to long line (>79 characters). Unable to shortern this line as it breaks the code.

## Further Testing

This site was designed for and tested across the following web browsers:
    - Google Chrome
    - Microsoft Edge
    - Mozilla Firefox
    - Opera
    - Safari

### Lighthouse Testing

- [Home](./documentation/images/testing/home-page-lighthouse.png)
  - The Lighthouse audit for the homepage (index.html) reflects strong overall performance across key metrics. The slightly lower performance score is primarily driven by the Largest Contentful Paint (LCP), resulting from image rendering times and external CDN dependencies; consequently, no immediate modifications were made based on this initial report.
- [The Edda Library](./documentation/images/testing/the-edda-library-lighthouse.png)
  - This page also demonstrates a strong overall score, with the exception of performance; this minor dip is driven entirely by the LCP, stemming from the same external asset and rendering factors identified on the homepage.
- [The Entity Archive](./documentation/images/testing/the-entity-archive-lighthouse.png)
  - This page also returned a strong Lighthouse report, with the performance rating impacted solely by the LCP.
- [The Forge](./documentation/images/testing/the-forge-lighthouse.png)
  - This page also returned a strong Lighthouse report, with the performance rating impacted solely by the LCP.
- [Lore Detail](./documentation/images/testing/lore-detail-lighthouse.png)
  - This page also returned a strong Lighthouse report, with the performance rating impacted solely by the LCP.
- [Entity Profile](./documentation/images/testing/entity-profile-lighthouse.png)
  - This page also returned a strong Lighthouse report, with the performance rating impacted solely by the LCP.
- [Log In](./documentation/images/testing/log-in-lighthouse.png)
  - This page also returned a strong Lighthouse report, with the performance rating impacted solely by the LCP.
- [Log Out](./documentation/images/testing/log-out-lighthouse.png)
  - This page also returned a strong Lighthouse report, with the performance rating impacted solely by the LCP.
- [Register](./documentation/images/testing/register-lighthouse.png)
  - This page achieves high scores across all four Lighthouse parameters due to its minimal layout and lightweight footprint.

## Bugs and Fixes

The following bugs and their corresponding fixes were identified and resolved during both the active development and formal testing phases of the project:

| **Bug** | **Cause** | **Fix** |
| --- | --- | --- |
| Server would not run | Caused by incorrect identifier in url path in urls.py | Amended path identifier from `<name:name>/` to `<str:name>/` |
| Superuser unable to sign back in | Caused by change in settings for email verification required | Fixed by going to django admin panel and manually verifying the email address |
| The Forge forms would not submit correctly | Caused by having two forms on the same page | Resolved by crating one relevant function in combination with a name element on the button which is then used in an if elif statement of the relevant function |
| Unable to access The Forge without being logged in | Caused by `@login_required` decorator in views.py, intended to prevent non-authenticated users from making posts | Removed this decorator and reverted to a different logic to get the desired outcome |
| Unable to see the SVG icon/s in in the forge submit button | Different ID's betweeen use tag and the SVG file | Updated ID's to match |
| Contact Developer form not functioning - email would not send | Caused by antivirus that contained an email shield function and causing a certification error | Turned off email shield |
| Contact developer message would be recieved as if the site has sent the email. In ability to reply to user who sent the email | Caused by functionality when using `send_mail` | Reverted to using `EmailMessage` which enabled a `reply_to` function |
| Submitting a Lore entry resulted in a reverse error | Caused by the slug not automatically populating | Updated the model to include slugify and self-populate to automatically generate this field |
| Mimir's Whispers section always rendering the default text | Caused by the `count()` logic being performed prior to `filter(status=1)` | Updated the function so the filter is performed before the count logic |
| Every entity in the database adding to the entities field for lore entries | Caused by logic with the ManytoManyfield | Implemented Select2 django package to improve functionality and resolve the issue |
| Edda Library sort function had the select items sat outside of dropdown box and weren't able to be selected | Caused by incorrect placement of `</select>` tag | Removed the tag |
| Clicking edit after clicking reply in comments section prepopulated the reply text area with the parent comment text with no text prepopulating the update comment text area | Caused by an issue with the JavaScript code logic | Updated JavaScript to get the specific comments text and injecting that into the update form. Also added in function to clear the reply text area when reply button is clicked |
| Clicking Next or Previous in the Edda Library resulted in the current sort selection reseting | Caused by a lack of code logic | Passed the current sort selection into the `href` link of the next/previous links |

## Future Improvements & Known Bugs

Future enhancements for the site will focus on optimizing user experience, streamlining the content moderation workflow, and resolving minor technical constraints identified during testing. These improvements include:

- *Non-Disruptive Content Edits*
  - Modifying the content moderation workflow so that edited lore entries or entity profiles remain publicly visible while their updates await review. Once approved, the new edits will seamlessly overwrite the live data, replacing the current system that reverts active posts to drafts during the approval process.
- *Modal Scroll Behavior Optimization*
  - Resolving a UI constraint in the lore update modal where interacting with the entity selection dropdown locks the scroll container, requiring users to click outside the selection field to resume scrolling.
- *Performance and LCP Enhancement*
  - Investigating and implementing optimization strategies to improve the site's overall Lighthouse performance rating, specifically focusing on reducing the Largest Contentful Paint (LCP) metric.
- *Advanced Relational Search* & *Kenning Search/Analysis*
  - Implement the pending features outlined in the [Scope Plane](./README.md/#scope-plane) that were deferred during the initial development phase of the project.
