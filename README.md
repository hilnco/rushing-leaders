# rushing-leaders
NEAP-stack (Node.js/Express/Angular/Postgres) app that loads JSON data from Superbowl XLIX, and displays the top rushers on a web app.

## Prequisites

1. PostgreSQL database (I used v9.4)
1. Python 2.6 or 3


## Quick Start

1. Clone the repo
1. Install dependencies via `npm install`
1. Start your Postgres server and create a database called "stats"
1. Create the database tables: `node server/data/create_table.js`
1. Start the server: `$ npm start`
1. If you do not have a 'postgres' user for your DB, you will need to update line 96 of server/data/load_data.py with your DB's user
1. Run server/data/load_data.py: python load_data.py
1. Navigate to http://localhost:3000 in your web browser. Only tested in Chrome.
