import { redirect } from "@sveltejs/kit";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async ({ locals, url }) => {
    if (!locals.user){
        const new_url = "/"+url.pathname.split("/")[1]+"/auth/login";
        throw redirect(303, new_url.replace("//", "/"));
    }

    return {user: locals.user};
}