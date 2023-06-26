// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			lang: string,
			user: {
				id: string,
				name: string,
				username: string,
				email: string,
				password: string,
				updated_at: Date,
				created_at: Date,
				session_token: string
			},
			settings: {
				display_mode: string
			}
		}
		// interface PageData {}
		// interface Platform {}
	}
}

export {};