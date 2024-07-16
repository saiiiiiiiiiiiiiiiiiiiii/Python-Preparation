import json


def load_data():
  try:
    with open('youtube.txt','r') as file:
      data = json.load(file)
      return data
  except FileNotFoundError:
    return [] or None

def list_all_video(Videos):
  pass
def Add_Video(Video):
  pass
def Update_video(Videos):
  pass
def Delete_video(Videos):
  pass

def main():

  Videos = load_data()
  while True:
    print("\n Youtube Manager")
    print("1. List a Favourite Videos")
    print("2. Add a youtube video ")
    print("3. Update a youtube video Details")
    print("4. Delete a youtube video")
    print("5. Exit the app")
    choice = input("Enter You're Choice")

    match choice:
      case "1":
        list_all_video(Videos)
      case "2":
        Add_Video(Videos)
      case "3":
        Update_video(Videos)
      case  "4":
        Delete_video(Videos)
      case "5":
          break
      case _:
          print("Invalid Choice")

          
if __name__ == "__main__":
  main()
      