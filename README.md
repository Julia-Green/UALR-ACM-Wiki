# UALR-ACM-Wiki

The UALR ACM Wiki is a small, wiki-style website that provides necessary information to both officers and members of the club. 
Information about officer positions, past events, club accounts, and standard operating procedures will be stored on this website. 
The prinicpal of least privelage will be implemted to limit access to wiki information pertaining to each user group.

## Data Model

### ACMUser (child of django.contrib.auth.models.AbstractUser)

- email : String (required)
- password: String (required)
- user-group: String (property)

## Site Functional Areas

### User Management

- Register New Users
- Log In / Log Out
- Update Existing Users
- Designate User Groups

### View Homepage

- Show site home/welcome page
- List all of the site pages a user has access to

### View Individual Pages

- Show individual pages of the wiki
- Redirect users to content management system for page editing

### Content Management

- Provide editing access to certian user groups