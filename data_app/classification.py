'''
This file of all classifications for points of interest uses the official Ordinance Survey 
classification system found in the /documentation folder of this repo 
or at https://www.ordnancesurvey.co.uk/documents/product-support/support/points-of-interest-classification-scheme.pdf
'''


# This dict of colours is strictly for groups at the moment - # TODO: Idea: make a shading-esque system for coloring within a group
color_map = {
          'Accommodation, eating and drinking': 'yellow', 
          'Commercial services': 'orange', 
          'Attractions': 'darkviolet', 
          'Sport and entertainment': 'limegreen', 
          'Education and health': 'red', 
          'Public Infrastructure': 'aquamarine', 
          'Manufacturing and production': 'slategray', 
          'Retail': 'violet', 
          'Transport': 'steelblue'}


groups = {'01': 'Accommodation, eating and drinking', 
          '02': 'Commercial services', 
          '03': 'Attractions', 
          '04': 'Sport and entertainment', 
          '05': 'Education and health', 
          '06': 'Public Infrastructure', 
          '07': 'Manufacturing and production', 
          '09': 'Retail', 
          '10': 'Transport'}


categories = {'01': 'Accommodation', 
              '02': 'Eating and drinking', 
              '03': 'Construction services', 
              '04': 'Consultancies', 
              '05': 'Employment and career agencies', 
              '06': 'Engineering services', 
              '07': 'Contract services', 
              '08': 'IT, advertising, marketing and media services', 
              '09': 'Legal and financial', 
              '10': 'Personal, consumer and other services', 
              '11': 'Property and development services', 
              '12': 'Recycling services', 
              '13': 'Repair and servicing', 
              '14': 'Research and design', 
              '15': 'Transport, storage and delivery', 
              '60': 'Hire services', 
              '16': 'Botanical and zoological', 
              '17': 'Historical and cultural', 
              '18': 'Recreational', 
              '19': 'Landscape features', 
              '20': 'Tourism', 
              '58': 'Bodies of water', 
              '21': 'Sport and entertainment support services', 
              '22': 'Gambling', 
              '23': 'Outdoor pursuits', 
              '24': 'Sports complex', 
              '25': 'Venues, stage and screen', 
              '26': 'Animal welfare', 
              '27': 'Education support services', 
              '28': 'Health practitioners and establishments', 
              '29': 'Health support services', 
              '31': 'Primary, secondary and tertiary education', 
              '32': 'Recreational and vocational education', 
              '33': 'Central and local government', 
              '34': 'Infrastructure and facilities', 
              '35': 'Organisations', 
              '37': 'Consumer products', 
              '38': 'Extractive industries', 
              '39': 'Farming', 
              '40': 'Foodstuffs', 
              '41': 'Industrial features', 
              '42': 'Industrial products', 
              '46': 'Clothing and accessories', 
              '47': 'Food, drink and multi item retail', 
              '48': 'Household, office, leisure and garden', 
              '49': 'Motoring', 
              '53': 'Air', 
              '54': 'Road and rail', 
              '55': 'Walking', 
              '56': 'Water', 
              '57': 'Public transport, stations and infrastructure', 
              '59': 'Bus transport'}


classes = {'0003': 'Bed and breakfast and backpacker accommodation', 
           '0007': 'Self catering', 
           '0002': 'Camping, caravanning, mobile homes, holiday parks and centres', 
           '0008': 'Timeshare', 
           '0005': 'Hostels and refuges for the homeless', 
           '0009': 'Youth accommodation', 
           '0006': 'Hotels, motels, country houses and inns', 
           '0012': 'Banqueting and function rooms', 
           '0020': 'Fish and chip shops', 
           '0013': 'Cafes, snack bars and tea rooms', 
           '0025': 'Internet Cafes', 
           '0018': 'Fast food and takeaway outlets', 
           '0034': 'Pubs, bars and inns', 
           '0019': 'Fast food delivery services', 
           '0043': 'Restaurants', 
           '0779': 'Building and component suppliers', 
           '0053': 'Glaziers', 
           '0045': 'Building contractors', 
           '0044': 'Metalworkers including blacksmiths', 
           '0046': 'Construction completion services', 
           '0054': 'Painting and decorating services', 
           '0047': 'Construction plant', 
           '0055': 'Plasterers', 
           '0048': 'Cutting, drilling and welding services', 
           '0056': 'Plumbing and heating services', 
           '0049': 'Demolition services',
           '0057': 'Pool and court construction',
           '0050': 'Diving services',
           '0058': 'Restoration and preservation services',
           '0051': 'Electrical contractors',
           '0059': 'Road construction services',
           '0778': 'Fencing and drystone walling services',
           '0060': 'Roofing and chimney services',
           '0052': 'Gardening, landscaping and tree surgery services',
           '0063': 'Architectural and building-related consultants', 
           '0069': 'Image consultants', 
           '0064': 'Business-related consultants', 
           '0070': 'Interpretation and translation consultants', 
           '0065': 'Computer consultants', 
           '0071': 'Security consultants', 
           '0066': 'Construction service consultants', 
           '0072': 'Telecommunications consultants', 
           '0067': 'Feng shui consultants, furnishers and shop fitters', 
           '0074': 'Traffic management and transport-related consultants', 
           '0068': 'Food consultants', 
           '0075': 'Careers offices and armed forces recruitment', 
           '0078': 'Employment agencies', 
           '0076': 'Domestic staff and home help', 
           '0079': 'Modelling and theatrical agencies', 
           '0077': 'Driver agencies', 
           '0081': 'Nursing agencies', 
           '0083': 'Aviation engineers', 
           '0089': 'Instrumentation engineers', 
           '0084': 'Chemical engineers', 
           '0090': 'Marine engineers and services', 
           '0085': 'Civil engineers', 
           '0091': 'Mechanical engineers', 
           '0086': 'Electrical and electronic engineers', 
           '0092': 'Pneumatic engineers', 
           '0087': 'Hydraulic engineers', 
           '0093': 'Precision engineers', 
           '0088': 'Industrial engineers', 
           '0094': 'Structural engineers', 
           '0095': 'Agricultural contractors', 
           '0102': 'Drain and sewage clearance', 
           '0096': 'Aircraft charters', 
           '0105': 'Linen hire and washroom services', 
           '0098': 'Catering services', 
           '0107': 'Office services', 
           '0100': 'Contract cleaning services', 
           '0108': 'Packers', 
           '0101': 'Display and window dressers', 
           '0109': 'Pest and vermin control', 
           '0114': 'Advertising services', 
           '0124': 'Internet services', 
           '0115': 'Artists, illustrators and calligraphers', 
           '0125': 'Literary services', 
           '0116': 'Computer security', 
           '0126': 'Mailing and other information services', 
           '0117': 'Computer systems services', 
           '0127': 'Marketing services', 
           '0118': 'Concert/exhibition organisers and services', 
           '0128': 'Plate makers, print finishers and typesetters', 
           '0119': 'Database services', 
           '0129': 'Press and journalism services', 
           '0120': 'Desktop publishing services', 
           '0130': 'Printing and photocopying services', 
           '0121': 'Electronic and Internet publishers', 
           '0131': 'Recording studios and record companies', 
           '0122': 'Film and video services', 
           '0133': 'Telephone, telex and fax services', 
           '0123': 'General computer services', 
           '0134': 'Television and radio services', 
           '0135': 'Accountants and auditors', 
           '0138': 'Banks and building societies', 
           '0137': 'Auctioneers, auction rooms and valuers', 
           '0796': 'Franchise and holding company services', 
           '0141': 'Cash machines', 
           '0148': 'Fundraising services', 
           '0142': 'Cheque cashing', 
           '0149': 'Insurers and support activities', 
           '0795': 'Commodity dealers', 
           '0150': 'Mortgage and financial lenders', 
           '0143': 'Company registration and trademarks', 
           '0151': 'Pawnbrokers', 
           '0144': 'Copyright and patent', 
           '0811': 'PayPoint® locations', 
           '0145': 'Credit reference agencies', 
           '0829': 'Pension and fund management', 
           '0140': 'Currency conversion and money transfers', 
           '0154': 'Solicitors, advocates and notaries public', 
           '0146': 'Debt collecting agencies', 
           '0773': 'Stocks, shares and unit trusts', 
           '0147': 'Financial advice services', 
           '0823': 'Adult services', 
           '0174': 'Party organisers', 
           '0155': 'Astrologers, clairvoyants and palmists', 
           '0175': 'Personalisation', 
           '0158': 'Cleaning services', 
           '0177': 'Photographic services', 
           '0160': 'Customer service centres', 
           '0826': 'Printing on garments', 
           '0161': 'CV writers', 
           '0775': 'Sculptors, woodworkers and stonemasons', 
           '0162': 'Detective and investigation agencies', 
           '0818': 'Sewage Services', 
           '0112': 'Event Ticket Agents and Box Office', 
           '0822': 'Slimming clubs and services', 
           '0165': 'Funeral and associated services', 
           '0821': 'Spas', 
           '0156': 'Hair and beauty services', 
           '0179': 'Sports services', 
           '0167': 'Headquarters, administration and central offices', 
           '0776': 'Tailoring and clothing alteration', 
           '0166': 'Historical research', 
           '0180': 'Tattooing and piercing services', 
           '0103': 'Hotel Booking Agencies', 
           '0182': 'Trophies and engraving services', 
           '0169': 'Introduction and dating agencies', 
           '0777': 'Vehicle breakdown and recovery services', 
           '0170': 'Lock, key and security services', 
           '0183': 'Vehicle cleaning services', 
           '0171': 'Message and greeting services', 
           '0185': 'Weather services', 
           '0173': 'Motoring organisations', 
           '0186': 'Wedding services', 
           '0774': 'Musicians, orchestras and composers', 
           '0188': 'Window cleaners', 
           '0189': 'Commercial property letting', 
           '0195': 'Property information services', 
           '0191': 'Estate and property management', 
           '0192': 'Property letting', 
           '0194': 'Property development services', 
           '0190': 'Property sales', 
           '0199': 'Clearance and salvage dealers', 
           '0200': 'Scrap metal dealers and breakers yards', 
           '0198': 'Rag merchants', 
           '0202': 'Waste paper merchants', 
           '0196': 'Recycling, reclamation and disposal', 
           '0204': 'Building repairs', 
           '0793': 'Shoe repairs', 
           '0205': 'Electrical equipment repair and servicing', 
           '0210': 'Sports and leisure equipment repair', 
           '0206': 'Household repairs and restoration', 
           '0211': 'Tool repairs', 
           '0207': 'Industrial repairs and servicing', 
           '0212': 'Vehicle repair, testing and servicing', 
           '0209': 'Service industry equipment repairs', 
           '0214': 'Design services', 
           '0217': 'Testing and analysis services', 
           '0216': 'Research services', 
           '0218': 'Airlines and airline services', 
           '0224': 'Ferry and cruise companies', 
           '0219': 'Animal transportation', 
           '0225': 'Import and export services', 
           '0221': 'Container and storage', 
           '0227': 'Railway related services', 
           '0222': 'Courier, delivery and messenger', 
           '0228': 'Removals and shipping agents', 
           '0223': 'Distribution and haulage', 
           '0230': 'Taxi services', 
           '0097': 'Boat hiring services',
           '0104': 'Leisure equipment hirings',
           '0270': 'Bouncy castles and inflatables hire',
           '0110': 'Renting and leasing of personal and household goods',
           '0159': 'Clothing hire',
           '0111': 'Sound, light and vision service and equipment hire',
           '0099': 'Construction and tool hire',
           '0113': 'Vehicle hire and rental',
           '0231': 'Aquaria and sea life centres',
           '0236': 'Horticultural attractions',
           '0232': 'Bird reserves, collections and sanctuaries',
           '0237': 'Salmon ladders',
           '0233': 'Butterfly farms',
           '0239': 'Zoos and animal collections',
           '0235': 'Farm-based attractions',
           '0240': 'Archaeological sites',
           '0244': 'Historic buildings including castles, forts and abbeys',
           '0813': 'Art galleries',
           '0246': 'Historical ships',
           '0241': 'Battlefields',
           '0248': 'Museums',
           '0245': 'Historic and ceremonial structures',
           '0252': 'Commons',
           '0254': 'Picnic areas',
           '0253': 'Country and national parks',
           '0255': 'Playgrounds',
           '0814': 'Municipal Parks and Gardens',
           '0257': 'Designated scenic features',
           '0259': 'Trigonometric points',
           '0268': 'Information centres',
           '0267': 'Sightseeing, tours, viewing and visitor centres',
           '0263': 'Laseria, observatories and planetaria',
           '0266': 'Theme and adventure parks',
           '0264': 'Model villages',
           '0269': 'Unspecified and other attractions',
           '0265': 'Railways (heritage, steam and miniature)',
           '0804': 'Lakes and waters',
           '0806': 'Tarns, pools and meres',
           '0805': 'Lochs and lochans',
           '0807': 'Reservoirs',
           '0271': 'Children\'s activity centres',
           '0275': 'Funfair services',
           '0273': 'Entertainment services',
           '0276': 'Mobile discos',
           '0274': 'Firework related services',
           '0820': 'Motorsport services',
           '0277': 'Amusement parks and arcades',
           '0279': 'Bookmakers',
           '0278': 'Bingo halls',
           '0280': 'Casinos',
           '0282': 'Angling and sports fishing',
           '0285': 'Parachuting and bungee jumping',
           '0283': 'Combat, laser and paintball games',
           '0286': 'Paragliding and hang-gliding',
           '0284': 'Hot air ballooning',
           '0321': 'Riding schools, livery stables and equestrian centres',
           '0770': 'Outdoor pursuit organisers and equipment',
           '0287': 'Water sports',
           '0289': 'Athletics facilities',
           '0299': 'Shooting facilities',
           '0290': 'Bowling facilities',
           '0300': 'Ski infrastructure and aerial cableways',
           '0291': 'Climbing facilities',
           '0301': 'Snooker and pool halls',
           '0292': 'Golf ranges, courses, clubs and professionals',
           '0302': 'Sports grounds, stadia and pitches',
           '0293': 'Gymnasiums, sports halls and leisure centres',
           '0303': 'Squash courts',
           '0294': 'Ice rinks',
           '0304': 'Swimming pools',
           '0297': 'Motorsport venues',
           '0305': 'Tennis facilities',
           '0298': 'Racecourses and greyhound tracks',
           '0306': 'Velodromes',
           '0825': 'Adult venues',
           '0312': 'Nightclubs',
           '0308': 'Cinemas',
           '0314': 'Social clubs',
           '0762': 'Conference and exhibition centres',
           '0315': 'Theatres and concert halls',
           '0316': 'Animal clipping and grooming',
           '0320': 'Pet cemeteries and crematoria',
           '0317': 'Dog training',
           '0322': 'Veterinarians and animal hospitals',
           '0318': 'Horse training',
           '0323': 'Veterinary pharmacies',
           '0319': 'Kennels and catteries',
           '0324': 'Education authorities',
           '0326': 'Examination boards',
           '0325': 'Education services',
           '0800': 'Secure units',
           '0780': 'Accident and emergency hospitals',
           '0370': 'Hospices',
           '0330': 'Alternative, natural and complementary',
           '0371': 'Hospitals',
           '0364': 'Chemists and pharmacies',
           '0372': 'Mental health centres and practitioners',
           '0365': 'Clinics and health centres',
           '0342': 'Midwifery',
           '0815': 'Day and Care Centres',
           '0373': 'Nursing and residential care homes',
           '0367': 'Dental and medical laboratories',
           '0344': 'Optometrists and opticians',
           '0368': 'Dental surgeries',
           '0809': 'Parenting and childcare services',
           '0335': 'Dental technicians',
           '0345': 'Physical therapy',
           '0337': 'Dieticians and nutritionists',
           '0352': 'Speech therapists',
           '0369': 'Doctors surgeries',
           '0354': 'Surgeons and cosmetic surgeries',
           '0333': 'Foot related services',
           '0812': 'Walk-in centres',
           '0340': 'Homeopaths',
           '0356': 'Ambulance and medical transportation services',
           '0106': 'Medical equipment rental and leasing',
           '0357': 'Blood transfusion service',
           '0361': 'Medical waste disposal services',
           '0358': 'Counselling and advice services',
           '0362': 'Pregnancy related services and help centres',
           '0359': 'Health authorities',
           '0363': 'X-ray services',
           '0379': 'Broad age range and secondary state schools',
           '0377': 'Independent and preparatory schools',
           '0375': 'First, primary and infant schools',
           '0801': 'Pupil referral units',
           '0376': 'Further education establishments',
           '0380': 'Special schools and colleges',
           '0381': 'Higher education establishments',
           '0382': 'Unspecified and other schools',
           '0384': 'Ballet and dance schools',
           '0394': 'Language schools',
           '0385': 'Beauty and hairdressing schools',
           '0395': 'Martial arts instruction',
           '0388': 'Diving schools',
           '0396': 'Music teachers and schools',
           '0389': 'Drama schools',
           '0397': 'Nursery schools and pre- and after-school care',
           '0390': 'Driving and motorcycle schools',
           '0399': 'Sailing schools',
           '0391': 'First aid training',
           '0400': 'Sports and fitness coaching',
           '0392': 'Flying schools',
           '0403': 'Training providers and centres',
           '0404': 'Armed services',
           '0416': 'Local government',
           '0415': 'Central government',
           '0419': 'Members of parliament and members of European parliament',
           '0407': 'Coastal Safety',
           '0422': 'Police stations',
           '0408': 'Consular services',
           '0424': 'Prisons',
           '0409': 'Courts, court services and tribunals',
           '0425': 'Probation offices and police support services',
           '0411': 'Driving test centres',
           '0426': 'Registrars offices',
           '0412': 'Embassies and consulates',
           '0417': 'Revenue and customs offices',
           '0414': 'Fire brigade stations',
           '0429': 'Social service activities',
           '0830': 'Foreign country support activities',
           '0431': 'Tribunals',
           '0418': 'Job centres',
           '0453': 'Allotments',
           '0459': 'Places of worship',
           '0454': 'Cemeteries and crematoria',
           '0461': 'Public toilets',
           '0455': 'Drinking fountains and water points',
           '0462': 'Recycling centres',
           '0433': 'Electrical features',
           '0440': 'Refuse disposal facilities',
           '0437': 'Gas features',
           '0442': 'Telecommunications companies',
           '0456': 'Halls and community centres',
           '0443': 'Telecommunications features',
           '0457': 'Letter boxes',
           '0444': 'Utility companies and brokers',
           '0458': 'Libraries',
           '0441': 'Waste storage, processing and disposal',
           '0438': 'Meteorological features',
           '0802': 'Wi-Fi hotspots',
           '0445': 'Animal welfare organisations',
           '0448': 'Institutes and professional organisations',
           '0816': 'Charitable organisations',
           '0449': 'Political parties and related organisations',
           '0769': 'Community networks and projects',
           '0450': 'Religious organisations',
           '0817': 'Conservation Organisations',
           '0447': 'Sports clubs and associations',
           '0446': 'Fan clubs and associations',
           '0452': 'Youth organisations',
           '0464': 'Baby, nursery and playground equipment',
           '0480': 'Footwear',
           '0790': 'Bathroom fixtures, fittings and sanitary equipment',
           '0481': 'Furniture',
           '0465': 'Beds and bedding',
           '0482': 'Garden goods',
           '0466': 'Brushes',
           '0483': 'Giftware',
           '0467': 'Candles',
           '0485': 'Hobby, sports and pastime products',
           '0468': 'Canvas goods',
           '0487': 'Jewellery, gems, clocks and watches',
           '0470': 'Carpets, flooring, rugs and soft furnishings',
           '0488': 'Lampshades and lighting',
           '0472': 'China and glassware',
           '0489': 'Leather products',
           '0473': 'Clothing, components and accessories',
           '0490': 'Lingerie and hosiery',
           '0785': 'Conservatories',
           '0491': 'Luggage, bags, umbrellas and travel accessories',
           '0474': 'Cookers and stoves - non-electrical',
           '0471': 'Medals, trophies, ceremonial and religious goods',
           '0475': 'Cosmetics, toiletries and perfumes',
           '0493': 'Musical instruments',
           '0476': 'Curtains and blinds',
           '0494': 'Photographic and optical equipment',
           '0477': 'Cutlery and tableware',
           '0479': 'Refrigeration and freezing appliances',
           '0478': 'Disability and mobility equipment',
           '0495': 'Saunas and sunbeds',
           '0486': 'Disposable products',
           '0497': 'Tents, marquees and camping equipment',
           '0782': 'Fireplaces and mantelpieces',
           '0498': 'Tobacco products',
           '0500': 'Coal mining',
           '0504': 'Sand, gravel and clay extraction and merchants',
           '0501': 'Oil and gas extraction, refinery and product manufacture',
           '0506': 'Stone quarrying and preparation',
           '0502': 'Ore mining',
           '0507': 'Unspecified quarries or mines',
           '0508': 'Animal breeders (not horses)',
           '0514': 'Fruit, flower and vegetable growers',
           '0509': 'Arable farming',
           '0516': 'Horse breeders and dealers',
           '0510': 'Bee-keepers',
           '0517': 'Livestock farming',
           '0511': 'Dairy farming',
           '0518': 'Mixed or unspecified farming',
           '0512': 'Fish and shellfish',
           '0520': 'Poultry farming, equipment and supplies',
           '0513': 'Forestry',
           '0522': 'Alcoholic drinks',
           '0525': 'Dairy products',
           '0523': 'Animal feeds, pet foods, hay and straw',
           '0526': 'Fish, meat and poultry products',
           '0524': 'Baking and confectionery',
           '0528': 'Milling, refining and food additives',
           '0530': 'Catering and non-specific food products',
           '0529': 'Non-alcoholic drink',
           '0531': 'Business parks and industrial estates',
           '0538': 'Pipelines',
           '0534': 'Energy production',
           '0542': 'Unspecified works or factories',
           '0536': 'Lime kilns',
           '0543': 'Water pumping stations',
           '0537': 'Oast houses',
           '0544': 'Abrasive products and grinding equipment',
           '0577': 'Industrial coatings and finishings',
           '0783': 'Access equipment',
           '0580': 'Lifting and handling equipment',
           '0545': 'Adhesives and sealants',
           '0581': 'Lubricants and lubricating equipment',
           '0546': 'Aeroplanes',
           '0582': 'Marine equipment including boats and ships',
           '0547': 'Agricultural machinery and goods',
           '0583': 'Measurement and inspection equipment',
           '0548': 'Air and water filtration',
           '0584': 'Medical equipment, supplies and pharmaceuticals',
           '0549': 'Arms and ammunition',
           '0585': 'Metals manufacturers, fabricators and stockholders',
           '0550': 'Bearing, gear and drive elements',
           '0586': 'Moulds, dies and castings',
           '0551': 'Bee-keeping supplies',
           '0588': 'Office and shop equipment',
           '0553': 'Bricks, tiles, clay and ceramic products',
           '0589': 'Ovens and furnaces',
           '0555': 'Cable, wire and fibre optics',
           '0590': 'Packaging',
           '0784': 'Car ports and steel buildings',
           '0591': 'Paints, varnishes and lacquers',
           '0557': 'Colours, chemicals and water softeners and supplies',
           '0594': 'Pesticides',
           '0558': 'Cleaning equipment and supplies',
           '0598': 'Printing-related machinery',
           '0562': 'Concrete products',
           '0599': 'Published goods',
           '0563': 'Cooling and refrigeration',
           '0600': 'Pumps and compressors',
           '0765': 'Educational equipment and supplies',
           '0601': 'Radar and telecommunications equipment',
           '0564': 'Electrical components',
           '0602': 'Road maintenance equipment',
           '0565': 'Electrical motors and generators',
           '0603': 'Ropes, nets and cordage',
           '0566': 'Electrical production and manipulation equipment',
           '0604': 'Rubber, silicones and plastics',
           '0567': 'Electronic equipment',
           '0605': 'Seals, tapes, taps and valves',
           '0568': 'Electronic media',
           '0791': 'Shelving, storage, safes and vaults',
           '0569': 'Engines',
           '0606': 'Signs',
           '0781': 'Fences, gates and railings',
           '0607': 'Special purpose machinery and equipment',
           '0571': 'Fertilisers',
           '0609': 'Stationery, stamps, tags and labels',
           '0572': 'Food and beverage industry machinery',
           '0608': 'Textiles, fabrics, silk and machinery',
           '0573': 'General construction supplies',
           '0579': 'Tools including machine shops',
           '0612': 'General manufacturing',
           '0615': 'Vehicles',
           '0574': 'General-purpose machinery',
           '0613': 'Vehicle bodybuilders',
           '0575': 'Glass',
           '0614': 'Vehicle components',
           '0788': 'Glass fibre services',
           '0787': 'Waste collection, processing and disposal equipment',
           '0576': 'Horticultural equipment',
           '0616': 'Wood products including charcoal, paper, card and board',
           '0767': 'Ice',
           '0617': 'Workwear',
           '0797': 'Baby and nursery equipment and children\'s clothes',
           '0659': 'Jewellery and fashion accessories',
           '0656': 'Clothing',
           '0660': 'Lingerie and hosiery',
           '0657': 'Footwear',
           '0671': 'Alcoholic drinks including off-licences and wholesalers',
           '0668': 'Green and new age goods',
           '0661': 'Bakeries',
           '0669': 'Grocers, farm shops and pick your own',
           '0662': 'Butchers',
           '0670': 'Herbs and spices',
           '0768': 'Cash and carry',
           '0703': 'Livestock markets',
           '0663': 'Confectioners',
           '0705': 'Markets',
           '0699': 'Convenience stores and independent supermarkets',
           '0672': 'Organic, health, gourmet and kosher foods',
           '0665': 'Delicatessens',
           '0819': 'Supermarket chains',
           '0666': 'Fishmongers',
           '0798': 'Tea and coffee merchants',
           '0667': 'Frozen foods',
           '0824': 'Adult shops',
           '0683': 'Garden centres and nurseries',
           '0712': 'Art and antiques',
           '0684': 'Garden machinery and furniture',
           '0674': 'Books and maps',
           '0685': 'General household goods',
           '0693': 'Camping and caravanning',
           '0717': 'Gifts and cards',
           '0675': 'Carpets, rugs, soft furnishings and needlecraft',
           '0686': 'Hobby, sports and pastime products',
           '0714': 'Charity shops',
           '0687': 'Leather goods, luggage and travel accessories including handbags',
           '0676': 'China and glassware',
           '0688': 'Lighting',
           '0827': 'Comic books',
           '0704': 'Mail order and catalogue stores',
           '0828': 'Computer shops',
           '0689': 'Music and video',
           '0720': 'Computer supplies',
           '0690': 'Musical instruments',
           '0677': 'Cosmetics, toiletries, perfumes and hairdressing supplies',
           '0718': 'Party goods and novelties',
           '0678': 'Craft supplies',
           '0691': 'Pets, supplies and services',
           '0679': 'Cycles and accessories',
           '0724': 'Photographic and optical equipment',
           '0700': 'Department stores',
           '0763': 'Post offices',
           '0701': 'Discount stores',
           '0831': 'Potteries',
           '0680': 'DIY and home improvement',
           '0719': 'Second-hand goods',
           '0721': 'Domestic appliances',
           '0708': 'Shopping centres and retail parks',
           '0722': 'Electrical goods and components',
           '0725': 'Stationery and office supplies',
           '0716': 'Florists',
           '0710': 'Surplus goods',
           '0682': 'Furniture',
           '0726': 'Telephones and telephone cards',
           '0766': 'Fuel distributors and suppliers',
           '0694': 'Travel agencies',
           '0764': 'Garages, garden and portable buildings',
           '0695': 'New vehicles',
           '0697': 'Vehicle auctions',
           '0696': 'Second-hand vehicles',
           '0698': 'Vehicle parts and accessories',
           '0728': 'Airports and landing strips',
           '0729': 'Helipads',
           '0730': 'Bridges',
           '0737': 'Petrol and fuel stations',
           '0733': 'Cattle grids',
           '0740': 'Signalling facilities',
           '0734': 'Fords and level crossings',
           '0743': 'Viaducts',
           '0735': 'Motorway service stations',
           '0744': 'Weighbridges',
           '0736': 'Parking',
           '0747': 'Footbridges',
           '0751': 'Aqueducts',
           '0753': 'Moorings and unloading facilities',
           '0760': 'Ferries and ferry terminals',
           '0754': 'Rivers and canal organisations and infrastructure',
           '0752': 'Locks',
           '0755': 'Weirs, sluices and dams',
           '0731': 'Bus and coach stations, depots and companies',
           '0758': 'Taxi ranks',
           '0794': 'London Underground entrances',
           '0756': 'Tram, metro and light railway stations and stops',
           '0738': 'Railway stations, junctions and halts',
           '0761': 'Underground network stations',
           '0732': 'Bus stops',
           '0759': 'Hail and ride zones'}

def get_lengths():
    print('Groups: ' + str(len(groups)))
    print('Categories: ' + str(len(categories)))
    print('Classes: ' + str(len(classes)))
