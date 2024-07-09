<script setup lang="ts">
import { ref } from "vue";
import { Sun, Moon } from "lucide-vue-next";
import { Button } from "@/components/ui/button";

const isDarkMode = ref(false);

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value;
  document.documentElement.classList.toggle("dark", isDarkMode.value);
};
</script>

<template>
  <header
    class="bg-pastel-200 dark:bg-pastel-800 p-4 flex justify-between items-center"
  >
    <slot name="left"></slot>
    <h1 class="text-2xl font-bold">My Static Site</h1>
    <Button @click="toggleDarkMode" variant="ghost" size="icon">
      <Sun v-if="isDarkMode" class="h-6 w-6" />
      <Moon v-else class="h-6 w-6" />
    </Button>
  </header>
</template>
