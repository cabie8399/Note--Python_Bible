from django.shortcuts import render

# Create your views here.

def home(request):

    import requests
    import json

    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)

    return render(request,'home.html',{"api":api})




def user(request):

    
    
    if request.method == "POST":

        import requests
        import json
        
        user = request.POST['user']
        user_req = requests.get("https://api.github.com/users/"+user)
        user_info = json.loads(user_req.content)
        
        return render(request,'user.html',{'user':user,'user_info':user_info})
    
    else:
        notfound = "請在搜索框中輸入要查詢的user..."
        return render(request,'user.html',{'notfound':notfound})



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    