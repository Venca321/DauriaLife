import { redirect, type Actions } from "@sveltejs/kit";

export const actions: Actions = {
    login: async ({ cookies, request, params }) => {
        const formData = await request.formData();
        const username_or_email = String(formData.get("username_or_email"));
        const password = String(formData.get("password"));
        const lang = params.lang || 'cz';

		const response = await fetch("http://backend:5002/api/user/auth/sign_in", {
            method: 'POST',
            body: JSON.stringify({"lang": lang, "username_or_email": username_or_email, "password": password}),
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
        throw redirect(303, `/${lang}/user/home`);
    }
}