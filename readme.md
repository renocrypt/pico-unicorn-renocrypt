Create project

- `pnpm create vite@latest temp-vue --template vue-ts`
- Move relevant files out
- `pnpm i`

Add Tailwind and its configuration

- `pnpm install -D tailwindcss autoprefixer`
- `pnpm dlx tailwindcss init -p`
- `pnpm i -D @types/node`

`vite.config`

```typescript
import path from "node:path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import tailwind from "tailwindcss";
import autoprefixer from "autoprefixer";

export default defineConfig({
  css: {
    postcss: {
      plugins: [tailwind(), autoprefixer()],
    },
  },
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
```

`tsconfig`

- `pnpm dlx shadcn-vue@latest init`
