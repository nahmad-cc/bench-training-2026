import requests

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"User not found: {username}")
            return
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return
        
        user = response.json()
        
        print(f"\nUser: {user['login']}")
        print(f"Name: {user['name']}")
        print(f"Bio: {user['bio']}")
        print(f"Repos: {user['public_repos']}")
        print(f"Followers: {user['followers']}")
        
        # get repos
        repos_url = f"https://api.github.com/users/{username}/repos?sort=stars&per_page=5"
        repos_res = requests.get(repos_url)
        
        if repos_res.status_code == 200:
            repos = repos_res.json()
            print("\nTop Repos:")
            for repo in repos:
                lang = repo['language'] if repo['language'] else 'N/A'
                print(f"  {repo['name']}: {repo['stargazers_count']} stars ({lang})")
    
    except:
        print("Error connecting to GitHub")

username = input("GitHub username: ")
fetch_github_user(username)
