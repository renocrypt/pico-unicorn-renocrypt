<script setup lang="ts">
import { ref } from "vue";
import { Menu } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import NavHeader from "@/components/NavHeader.vue";
import Sidebar from "@/components/Sidebar.vue";

const isSidebarOpen = ref(false);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};
</script>

<template>
  <div
    class="min-h-screen bg-pastel-100 dark:bg-pastel-900 text-pastel-900 dark:text-pastel-100"
  >
    <NavHeader>
      <template #left>
        <Button @click="toggleSidebar" variant="outline" size="icon">
          <Menu class="h-6 w-6" />
        </Button>
      </template>
    </NavHeader>

    <div class="flex">
      <Sidebar :isOpen="isSidebarOpen" @close="isSidebarOpen = false">
        <!-- Add your sidebar content here -->
      </Sidebar>

      <!-- Main Content -->
      <main class="flex-grow p-8 ml-0 md:m-auto">
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
