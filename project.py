import json



def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def helper_method(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)



def list_all_videos(videos):
    print("\n")
    print("*" * 60)
    for index, vedio in enumerate(videos,start=1):
        print(f"{index}. Video name : {vedio['name']} , duration : {vedio['time']}")
    print("\n")
    print("*" * 60)   


def add_youtube_video(videos):
    name=input("Enter video name : ")
    time=input("Enter video time : ")
    videos.append({"name" : name,"time" : time})
    helper_method(videos)



def update_youtube_video(videos):
    list_all_videos(videos)
    choi=int(input("Enter the number that you want to update : "))
    if 1 <= choi <= len(videos):
        name=input("Enter youtube name : ")
        time=input("Enter youtube time : ")
        videos[choi-1]={'name' : name, 'time' : time}
        helper_method(videos)
    else: 
        print("Please choice a valid number ....")



def delete_youtube_video(videos):
    list_all_videos(videos)
    choi=int(input("Enter your video number that you want to delete :"))
    if 1 <= choi <= len(videos):
        del videos[choi-1]
        helper_method(videos)
    else:
        print("Enter a valid youtube number")


def main():
    videos=load_data()
    while True:
        print("\n........ Youtube manger | choode an option.........")
        print("1. List all Youtube Video")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube Video")
        print("5. Exit the app")
        choic=input("Enter your choice : ")

        match choic:
            case '1':
                list_all_videos(videos)
            case '2':
                add_youtube_video(videos)
            case '3':
                update_youtube_video(videos)
            case '4':
                delete_youtube_video(videos)
            case '5':
                break
            case _:
                print("..............Invalid choice........")

if __name__=="__main__":
    main()
