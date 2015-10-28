/*
Was not able to get this to work as expected, turned to python for the json parsing and postgres insert
*/

var data = require('./data.json');

var i, periods, j, pbp, k, events, l, statistics;

for (i = 0; i < data.periods.length; i++) {
	periods = data.periods[i];

	for (j = 0; j < periods.pbp.length; j++) {
		pbp = periods.pbp[j];

		if ('events' in pbp) {
			for (k = 0; k < pbp.events.length; k++) {
				events = pbp.events[k];

				if ('statistics' in events) {
					for (l = 0; l < events.statistics.length; l++) {
						statistics = events.statistics[i];
						console.log(JSON.stringify(statistics));
		            }
		        }
	        }
	    }
	}
}
