# -*- coding: utf8 -*-
"""
 Generate some bogus city data.
"""
import csv
import random
import sys

city = ['Abbotsford', 'Armstrong', 'Burnaby', 'Campbell River', 'Castlegar', 'Chilliwack', 'Colwood', 'Coquitlam', 'Courtenay', 'Cranbrook', 'Dawson Creek', 'Duncan', 'Enderby', 'Fernie', 'Fort St. John', 'Grand Forks', 'Greenwood', 'Kamloops', 'Kelowna', 'Kimberley', 'Kitimat', 'Langford', 'Langley', 'Merritt', 'Nanaimo', 'Nelson', 'New Westminster', 'North Vancouver', 'Parksville', 'Penticton', 'Pitt Meadows', 'Port Alberni', 'Port Coquitlam', 'Port Moody', 'Powell River', 'Prince George', 'Prince Rupert', 'Quesnel', 'Revelstoke', 'Richmond', 'Rossland', 'Salmon Arm', 'Surrey', 'Terrace', 'Trail', 'Vancouver', 'Vernon', 'Victoria', 'White Rock', 'Williams Lake']
def get_city():
	return random.choice(city)

street = ['Amber','Anchor','Acres', 'Blue','Apple','Arbor', 'Bright','Autumn','Avenue', 'Broad','Barn','Bank', 'Burning','Beacon','Bend', 'Cinder','Bear','Canyon', 'Clear','Berry','Chase', 'Colonial','Blossom','Circle', 'Cotton','Bluff','Corner', 'Cozy','Branch','Court', 'Crystal','Brook','Cove', 'Dewy','Butterfly','Crest', 'Dusty','Cider','Dale', 'Easy','Cloud','Dell', 'Emerald','Creek','Edge', 'Fallen','Dale','Estates', 'Foggy','Deer','Falls', 'Gentle','Elk','Farms', 'Golden','Embers','Gardens', 'Grand','Fawn','Gate', 'Green','Forest','Glade', 'Harvest','Fox','Glen', 'Hazy','Gate','Grove', 'Heather','Goose','Highlands', 'Hidden','Grove','Hollow', 'High','Hickory','Isle', 'Honey','Hills','Jetty', 'Indian','Horse','Knoll', 'Iron','Island','Landing', 'Jagged','Lagoon','Lane', 'Lazy','Lake','Ledge', 'Little','Leaf','Manor', 'Lost','Log','Meadow', 'Merry','Mountain','Mews', 'Middle','Nectar','Nook', 'Misty','Oak','Orchard', 'Noble','Panda','Park', 'Old','Pine','Path', 'Pleasant','Pioneer','Pike', 'Quaking','Pond','Place', 'Quiet','Pony','Point', 'Red','Prairie','Promenade', 'Rocky','Quail','Ridge', 'Round','Rabbit','Round', 'Rustic','Rise','Run', 'Shady','River','Stead', 'Silent','Robin','Swale', 'Silver','Shadow','Terrace', 'Sleepy','Sky','Trace', 'Stony','Spring','Trail', 'Sunny','Timber','Vale', 'Tawny','Treasure','Valley', 'Thunder','View','View', 'Umber','Wagon','Vista', 'Velvet','Willow','Way', 'Wishing','Zephyr','Woods']
def get_street():
	num = random.randint(1, 9999)
	n = random.randint(1,3)
	return "%s %s" % (num, " ".join([random.choice(street) for _ in xrange(n)]))

def get_phone():
	npa = random.randint(200, 800)
	num = random.randint(2000000, 2001000)
	return "%s%s" % (npa, num)

bnames = ['Ameredia', 'AKQA', 'Automattic', 'Duncan/Channon', 'Goodby, Silverstein & Partners', 'SALT Branding', '4delite', 'Apparel', 'Gap, Inc. ', 'Levi Strauss & Co.', 'Gymboree', 'Beauty', 'Bare Escentuals', 'Benefit', 'Sephora', 'Biomedical', 'McKesson Corporation ', 'Construction & Real Estate', 'AMB Property Corporation', 'Bechtel', 'BRE Properties', 'Digital Realty Trust', 'LoopNet', 'Electronics', 'Dolby Laboratories', 'FusionStorm', 'Sega of America', 'Watkins Computer, Inc', 'Energy', 'Pacific Gas & Electric ', 'Entertainment', 'Industrial Light & Magic', 'Lucasfilm', 'LucasArts', 'SHN ', 'Financial', 'Bank of the West', 'Bank of the Orient', 'Charles Schwab ', 'Esurance', 'First Republic Bank', 'KKR Financial Holdings', 'Liquid Realty Partners', 'Pegasus Aviation', 'Stone & Youngberg, LLC', 'ThinkEquity Partners, LLC', 'Thomas Weisel Partners', 'UnionBanCal Corporation and Union Bank of California', 'VISA', 'Wells Fargo & Co. and Wells Fargo Bank ', 'WR Hambrecht + Co', 'Food and Drink', 'Ghiradelli', 'Adina World Beat Beverages', 'Anchor Brewing Company', 'Boudin Bakery', 'Del Monte Foods', 'Jack & Jasons Pancakes & Waffles', 'TCHO', 'Skyy Spirits', 'Internet', 'AfterCollege, Inc.', 'BitTorrent Inc.', 'Blogspot', 'Craigslist', 'Digg', 'Flickr', 'Kink.com', 'Linden Lab', 'Notehall', 'OpenTable', 'RarityGuide, Inc', 'Revision3', 'Square, Inc.', 'Salesforce.com', 'SixApart', 'Tapjoy', 'Technorati', 'Twitter', 'Trulia, Inc.', 'TypePad', 'Whiskey Media', 'Wikimedia Foundation', 'Yammer', 'Yelp, Inc.', 'YouNoodle', 'Zynga', 'Media', 'AllBusiness.com', 'Americana exchange', 'Bebo', 'CBS Interactive', 'Chronicle Books', 'CNET', 'Craigslist', 'Current TV', 'High Speed Productions', 'Juxtapoz', 'Thrasher', 'Dwell', 'LiveJournal', 'MacWorld Magazine', 'Mevio', 'Mother Jones Magazine', 'PC World Magazine', 'VIZ Media', 'Wired Magazine', 'XLR8R Magazine', 'Miscellany / Etc.', 'ABM Industries', 'Advent Software', 'Ammunition LLC', 'Blue Shield of California', 'Catholic Healthcare West', 'FusionStorm', 'Medivation', 'Recology', 'Schlage', 'State Compensation Insurance Fund', 'URS', 'Mirion Technologies', 'Non-profit', 'Electronic Frontier Foundation', 'Internet Archive', 'Room To Read', 'The Sierra Club', 'Wikimedia Foundation', 'Public Relations', 'Sparkpr', 'Professional Services', 'Elanex', 'Onyx Research, Inc.', 'Retail', 'Good Vibrations', 'Gymboree Corporation', 'Williams-Sonoma, Inc.', 'Travel', 'Artisan Travel', 'Apparel', 'Bebe ', 'The North Face ', 'Mountain Hardwear ', 'JanSport ', 'Marmot ', 'Western Mountaineering ', 'Biomedical', 'Buck Institute for Age Research ', 'Chiron ', 'Genentech ', 'Gilead Sciences ', 'Healthcare Kaiser Permanente ', 'Consumer Goods', 'Clorox ', 'Tesla Motors ', 'Electronics', 'AMD ', 'Adaptec ', 'Agilent Tech. ', 'Anchor Bay Technologies ', 'Apple Inc. ', 'Adaptec ', 'Applied Materials ', 'Bay Imaging ', 'Cisco Systems ', 'E-mu Systems ', 'Fujitsu Computer Products of America ', 'Genesis Microchip ', 'Hewlett Packard ', 'Hitachi Global Storage Technologies ', 'Hitachi Data Systems ', 'Intel ', 'JDS Uniphase ', 'Integrated Device Technology ', 'Logitech ', 'LSI Corporation ', 'Macrotron Systems, Inc. ', 'Maxtor ', 'Monster Cable Products ', 'National Semiconductor ', 'NetApp ', 'Nvidia ', 'Philips Lumileds Lighting Company ', 'Rackable Systems ', 'Rambus ', 'Sanmina-SCI ', 'SanDisk ', 'Seagate Technology ', 'Silicon Graphics ', 'Solectron Corporation ', 'Sony Optiarc America Inc. ', 'Sun Microsystems ', 'Supermicro ', 'Super Talent ', 'THX ', 'Digidesign ', 'Juniper Networks ', 'Foundry Networks ', 'Terayon ', 'Xilinx ', 'Energy', 'Calpine Corporation ', 'Chevron ', 'Entertainment', 'Electronic Arts ', 'Kerner Optical ', 'Netflix ', 'Pandora ', 'Pixar ', 'Dreamworks Animation ', 'Skywalker Sound ', 'Lucasfilm Animation ', 'Sony Computer Entertainment America Inc. ', 'Financial', 'Fisher Investments ', 'Franklin Templeton Investments ', 'PayPal ', 'Robert Half International ', 'Food and Drink', 'Amadillo Willys ', 'Basic American Foods ', 'Black Angus Steakhouse ', 'C&H Pure Cane Sugar ', 'Clif Bar ', 'Dreyers Grand Ice Cream ', 'Häagen-Dazs ', 'Jamba Juice ', 'Jelly Belly ', 'Odwalla ', 'Peets Coffee & Tea ', 'PowerBar ', 'Sees Candies ', 'Internet', 'Ask.com ', 'eBay ', 'Google ', 'Yahoo! ', 'YouTube ', 'Facebook ', 'Media', 'University of California Press ', 'Communication Arts ', 'Other', 'Firemans Fund Insurance Company ', 'Retail', 'Orchard Supply Hardware ', 'Ross Stores ', 'Safeway ', 'Shutterfly ', 'Restoration Hardware ', 'Walmart.com ', 'Tiny Prints ', 'Software', 'Adobe Systems ', 'Autodesk ', 'Business Objects ', 'Intuit ', 'McAfee ', 'Mozilla ', 'Oracle ', 'Skytide ', 'Sybase ', 'Symantec ', 'VMware ', 'Tibco ', 'Security', 'Franklin Resources ', 'Sports', 'Pac-10 Conference ', 'Specialized Bicycle Components ', 'Lowepro ', 'Hydrapak LLC ', 'Fox Racing ', 'Giro ', 'Transportation and Logistic', 'Virgin America ', 'Con-way ', 'Telecommunications', 'Calix, Inc. Petaluma, California']
def get_name():
	return random.choice(bnames)


writer = csv.writer(open(sys.argv[1], 'wb'))

writer.writerow((
	'id',
	'name',
	'prov',
	'city',
	'street',
	'phone'
))
for i in xrange(10000):
	writer.writerow((
		i,
		get_name(),
		'BC',
		get_city(),
		get_street(),
		get_phone()
	))
