import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/kit/vite';
import httpProxy from 'http-proxy';

const config = {
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter(),
  },
};

const proxy = httpProxy.createProxyServer({
  target: 'http://localhost:5002',
  changeOrigin: true,
  pathRewrite: {
    '^/api': '', // Odstraní předponu /api ze zdrojové cesty
  },
});

export default { ...config, vite: { ...config.vite, server: { middleware: [proxy] } } };
