import {API} from '../../backend';
import { isAuthenticated } from '../../auth/helper';

export const testlist = () => {
        const userId = isAuthenticated() && isAuthenticated().user.id;
        return fetch(`${API}quizes/testlist/${userId}/`,{
            method : "GET"
        })
        .then((response) => {
            return response.json()
            
        })
        .catch((err) => console.log(err))
};

export const history = () => {
    const userId = isAuthenticated() && isAuthenticated().user.id;
    return fetch(`${API}results/history/${userId}/`,{
        method : "GET"
    })
    .then((response) => {

        return response.json()
        
    })
    .catch((err) => console.log(err))
};