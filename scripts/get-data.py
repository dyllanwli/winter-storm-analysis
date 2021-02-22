import twint
import nest_asyncio
nest_asyncio.apply()

c = twint.Config()
# c.Custom["hashtags"] = ["id", "username"]
# c.Limit = 1000
c.Since = "2020-02-14"
c.Geo = "31.0000,-99.00000,600km"
c.Output = "../data/from20200214.csv"


# set up storage
# c.Pandas = True
# c.Location = True

# c.Store_json = True
c.Hide_output = True
c.Store_csv = True
c.Count = True
# c.Profile_full = True # only works on username
c.Filter_retweets = False

twint.run.Search(c)