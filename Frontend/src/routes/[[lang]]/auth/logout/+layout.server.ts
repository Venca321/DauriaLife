import { redirect } from '@sveltejs/kit';

export function load({ cookies, url }) {
    cookies.set("session", "", {
        path: "/",
        expires: new Date(0)
    })
    
    const new_url = url.pathname.replace("/auth/logout", "/auth/login");
    throw redirect(302, new_url);
}