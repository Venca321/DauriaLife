import { redirect, type Actions } from "@sveltejs/kit";

export const actions: Actions = {
    register: async ({ cookies, request }) => {
        const formData = await request.formData();
        const username = String(formData.get("username"));
        const email = String(formData.get("email"));
        const password = String(formData.get("password"));
        const repeat_password = String(formData.get("password2"));

        const response = await fetch('http://localhost:5002/api/register', {
            method: 'POST',
            body: JSON.stringify({
                "username": username, 
                "email": email,
                "password": password,
                "repeat_password": repeat_password
            })
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