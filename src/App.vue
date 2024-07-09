<script setup lang="ts">
import { ref } from "vue";
import { Sun, Moon, Menu } from "lucide-vue-next";
import { Button } from "@/components/ui/button";

const isDarkMode = ref(false);
const isSidebarOpen = ref(false);

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value;
  document.documentElement.classList.toggle("dark", isDarkMode.value);
};

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};
</script>

<template>
  <div
    :class="{ dark: isDarkMode }"
    class="min-h-screen bg-pastel-100 dark:bg-pastel-900 text-pastel-900 dark:text-pastel-100"
  >
    <!-- Navigation Header -->
    <header
      class="bg-pastel-200 dark:bg-pastel-800 p-4 flex justify-between items-center"
    >
      <Button @click="toggleSidebar" variant="ghost" size="icon">
        <Menu class="h-6 w-6" />
      </Button>
      <h1 class="text-2xl font-bold">My Static Site</h1>
      <Button @click="toggleDarkMode" variant="ghost" size="icon">
        <Sun v-if="isDarkMode" class="h-6 w-6" />
        <Moon v-else class="h-6 w-6" />
      </Button>
    </header>

    <div class="flex">
      <!-- Sidebar -->
      <aside
        :class="{
          'translate-x-0': isSidebarOpen,
          '-translate-x-full': !isSidebarOpen,
        }"
        class="w-64 bg-pastel-300 dark:bg-pastel-700 p-4 fixed h-full transition-transform duration-300 ease-in-out"
      >
        <h2 class="text-xl font-semibold mb-4">Articles</h2>
        <!-- Add your sidebar content here -->
      </aside>

      <!-- Main Content -->
      <main class="flex-grow p-8 ml-0 md:ml-64">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<style>
@import "@/styles.css";

/* Custom Pastel Color Palette */
:root {
  --pastel-100: #f0f4f8;
  --pastel-200: #d9e2ec;
  --pastel-300: #bcccdc;
  --pastel-400: #9fb3c8;
  --pastel-500: #829ab1;
  --pastel-600: #627d98;
  --pastel-700: #486581;
  --pastel-800: #334e68;
  --pastel-900: #243b53;
}

.dark {
  --pastel-100: #243b53;
  --pastel-200: #334e68;
  --pastel-300: #486581;
  --pastel-400: #627d98;
  --pastel-500: #829ab1;
  --pastel-600: #9fb3c8;
  --pastel-700: #bcccdc;
  --pastel-800: #d9e2ec;
  --pastel-900: #f0f4f8;
}

/* Add any global styles here */
</style>
