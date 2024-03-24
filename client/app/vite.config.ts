import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    open: false,
    port: 3500,
  },
  build: {
    manifest: true, 
    rollupOptions: {
      output: {
        dir: '../dist',
        assetFileNames: "assets/[name].[ext]",
        entryFileNames: "assets/js/[name].min.js",
      },
    },
  },
});
