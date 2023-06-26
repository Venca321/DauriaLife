import { redirect, type Actions } from "@sveltejs/kit";

export const actions: Actions = {
    register: async ({ cookies, request, params }) => {
        const formData = await request.formData();
        const name = String(formData.get("name"));
        const username = String(formData.get("username"));
        const email = String(formData.get("email"));
        const password = String(formData.get("password"));
        const repeat_password = String(formData.get("password2"));
        const lang = params.lang || 'cz';

        if(password != repeat_password){
            return;
        }

        const response = await fetch('http://backend:5002/api/user/auth/register', {
            method: 'POST',
            body: JSON.stringify({
                "lang": lang,
                "name": name,
                "username": username, 
                "email": email,
                "password": password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();

        if(!data["session_token"]){ 
            return;
        };

        cookies.set("session", data["session_token"], {
            path: "/",
            httpOnly: true,
            sameSite: "strict",
            secure: process.env.NODE_ENV == "production",
            maxAge: 60 * 60 * 24 * 7
        });
        throw redirect(303, "/user/home");
    }
}