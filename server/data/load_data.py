import json
import psycopg2
import sys


#-----------------------------------------------------------------
# BEGIN PROCESSING JSON FILE
#-----------------------------------------------------------------		

#open data file
with open('data.json') as data_file:    
	data = json.load(data_file)

#start with periods list
periods = data['periods']

#iterate over lists and filter to pbp => events => statistics
pbp_list = []
for i, pbp in enumerate(d['pbp'] for d in periods): 
	pbp_list.append(pbp)

i = 0
events_list = []
for i in pbp_list:
	#iterate over nested lists
	j = 0
	for j in i:
		#if dictionary contains key 'events', push to list
		if j.get('events', False):
			events_list.append(j['events'])
i = 0
stats_list = []
for i in events_list:
	j = 0
	for j in i:
		if j.get('statistics', False):
			stats_list.append(j['statistics'])


#-----------------------------------------------------------------
# CREATE RECORD FOR INSERT INTO DATABASE
#-----------------------------------------------------------------

i = 0
for i in stats_list:
	j = 0
	for j in i:
		#player info
		if j.get('player', False):
			player_name = (j['player']['name'])
			player_jersey = (j['player']['jersey'])
			player_position = (j['player']['position'])
		else:
			player_name = None;
			player_jersery = None;
			player_position = None;

		#team info
		if j.get('team', False):
			team_alias = (j['team']['alias'])
			team_market = (j['team']['market'])
			team_name = (j['team']['name'])
		else:
			team_alias = None;
			team_market = None;
			team_name = None;

		#stat type
		if j.get('stat_type', False):
			stat_type = (j['stat_type'])
		else:
			stat_type = None

		#yards
		if j.get('yards', False):
			yards = (j['yards'])
		else:
			yards = None

		#inside 20
		if j.get('inside_20', False):
			inside_20 = (j['inside_20'])
		else:
			inside_20 = None

		query = "INSERT INTO stats (player_name, player_jersey, player_position, team_alias, team_market, team_name, stat_type, yards, inside_20) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
		data = (player_name, player_jersey, player_position, team_alias, team_market, team_name, stat_type, yards, inside_20)



		#-----------------------------------------------------------------
		# PERFORM INSERT INTO DATABASE
		#-----------------------------------------------------------------

		try:
		    conn=psycopg2.connect("dbname='stats' user='postgres'")
		except:
		    print ('Unable to connect to database.')
		    
		cur = conn.cursor()

		#try row insert
		try:
		    cur.execute(query, data)
		    conn.commit()
		except psycopg2.DatabaseError, e:
			print 'Error %s' % e
			sys.exit(1)
		finally:
			if conn:
				conn.close()
		


