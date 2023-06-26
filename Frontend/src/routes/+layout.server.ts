import { redirect } from "@sveltejs/kit";

/** @type {import('./$types').PageLoad} */
export function load({ locals, params, url }) {
  let new_lang = params.lang || 'cz';
  const langs = ["cz", "en"]
  
  if(!langs.includes(new_lang)) {
    throw redirect(300, url.pathname.replace("/" + new_lang, "/cz"));
  }

  locals.lang = new_lang;

  return {
    lang: new_lang
  };
}