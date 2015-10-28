var pg = require('pg');
var path = require('path');
var connectionString = require(path.join(__dirname, '../', '../', 'config'));

var client = new pg.Client(connectionString);
client.connect();
var query = client.query('CREATE TABLE stats(id SERIAL PRIMARY KEY, player_name VARCHAR(40), player_jersey VARCHAR(10), player_position VARCHAR(40), team_alias VARCHAR(10), team_market VARCHAR(40), team_name VARCHAR(40), stat_type VARCHAR(40), yards smallint, inside_20 smallint)');
query.on('end', function() { client.end(); });