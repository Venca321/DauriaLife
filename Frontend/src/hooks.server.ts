import type { Handle } from "@sveltejs/kit"

export const handle: Handle = async ({event, resolve}) => {
    const session = event.cookies.get("session")

    if (!session){
        return await resolve(event)
    }

    const response = await fetch('http://localhost:5002/api/session_login', {
        method: 'POST',
        body: JSON.stringify({"session_token": session})
    });
    const data = await response.json();

    const user = {
        id: data["id"],
        name: data["name"],
        username: data["username"],
        email: data["email"],
        password: data["password"],
        updated_at: data["updated_at"],
        created_at: data["created_at"],
        session_token: session
    }

    if (user){
        event.locals.user = user

        try{
            const response2 = await fetch('http://localhost:5002/api/user/settings/get', {
                method: 'POST',
                body: JSON.stringify({"id": user.id})
            });
            const data2 = await response2.json();
            const settings = {
                display_mode: data2["display_mode"]
            }

            event.locals.settings = settings
        }
        catch{}
    }

    return await resolve(event)
}