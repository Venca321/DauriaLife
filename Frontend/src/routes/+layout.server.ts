import { redirect } from "@sveltejs/kit";

/** @type {import('./$types').PageLoad} */
export function load({ params, url }) {
  let new_lang = params.lang || 'cz';
  const langs = ["cz", "en"]
  
  if(!langs.includes(new_lang)) {
    throw redirect(300, url.pathname.replace("/" + new_lang, "/cz"));
  }

  return {
    lang: new_lang
  };
}