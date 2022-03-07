import {API} from '../../backend';

export const signup = (user) => {
    return fetch(`${API}user/signup/`,{
        method : "POST",
        headers:{
            Accept : "application/json",
            "Content-Type" :"application/json"
        },
        body : JSON.stringify(user)
    })
    .then((response) => {
        return response.json();
    })
    .catch(err => console.log(err))
}

export const signin = (user) =>{
    const formData = new FormData()
    for (const name in user){
        formData.append(name,user[name])
    }

    return fetch(`${API}user/signin/`,{
        method : "POST",
        body : formData
    })
    .then((response) => {
        return response.json();
    })
    .catch((err) => console.log(err));
};

export const authenticate = (data,next) => {
    if(typeof window!==undefined){
        localStorage.setItem("jwt",JSON.stringify(data));
        next();
    }
}

export const isAuthenticated = () =>{
    if(typeof window==undefined){
    
       return false
    }
    if(localStorage.getItem("jwt")){
        return JSON.parse(localStorage.getItem("jwt"))
    }else{
    
        return false
    }
}

export const signout = next =>{
    const userId = isAuthenticated() && isAuthenticated().user.id;
    if(typeof window !== undefined){
        localStorage.removeItem("jwt");

        return fetch(`${API}user/signout/${userId}`,{
            method : "GET"
        })
        .then((response) => {
            console.log("Signout");
            next()
        })
        .catch((err) => console.log(err))
    }
}