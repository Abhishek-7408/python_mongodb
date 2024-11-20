from pymongo import MongoClient


client = MongoClient("mongodb+srv://youtubepy:<youtubepy>@connect.lvv0k.mongodb.net/" ,tlsAllowInvalidCertificates=True)


db = client["ytmanager"]
video_collection = db["videos"]


print(video_collection)

def add_video(name,time):
    video_collection.insert_one({"name":name, "time":time})


def list_video():
    for video in video_collection.find():
        print(f"ID:  {video['_id']}, Name:{video['name']} and Time:{video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id':video_id},{"$set":{"name": new_name,"time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({"_id":video_id})


def main():
    while True:
        print("\n Youtube Manager App")
        print("1.list all videos")
        print("2. add new video")
        print("3.update video")
        print("4.delete video")
        print("5.exit app")


        choice = input("Enter Your Choice : ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter Video name ")
            time = input("Enter Video time")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter video id: ")
            name = input("Enter  updated Video name ")
            time = input("Enter updated Video time")
            update_video(video_id,name, time)

        elif choice == '4':
            video_id = input("Enter video id: ")
         
            delete_video(video_id)

        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    





if __name__ == "__main__":
    main()


