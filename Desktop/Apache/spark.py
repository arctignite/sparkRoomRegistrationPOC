from ciscosparkapi import CiscoSparkAPI
import sys

bearer = "NmMxMDkzOWItNjIxZi00Nzg3LWJiMzItYmRmMDNlY2Q1NjVmYmViYzE2NjQtMGNl"
targetEmail = sys.argv[2]
name = sys.argv[1]
roomID = sys.argv[3]
textInput = "Hi " + name + "! Thanks for reserving a meeting room " + roomID + ". Please watch the videos below carefully. please be advised that you can find further information here: www.cisco.com"
videoURL = "https://www.youtube.com/watch?v=J4mMcy5OWz4"
imageURL = "https://www.ciscospark.com/content/dam/ciscospark/eopi/country/usa/home/HpMobileHero-767x479.jpg"


spark = CiscoSparkAPI(access_token=bearer)

print("spark succesfully init")

spark.messages.create(toPersonEmail=targetEmail, text=textInput)
spark.messages.create(toPersonEmail=targetEmail, text=videoURL)
spark.messages.create(toPersonEmail=targetEmail, files=["test.docx"])
spark.messages.create(toPersonEmail=targetEmail, files=[imageURL])

