<script setup lang="ts">
import { Skeleton } from "@/components/ui/skeleton";

defineProps<{
  content: string;
  isLoading: boolean;
  codeThemeClasses: string;
}>();
</script>

<template>
  <div v-if="isLoading" class="space-y-4">
    <Skeleton class="w-full h-4" v-for="n in 5" :key="n" />
  </div>
  <div
    v-else
    class="prose dark:prose-invert max-w-none"
    :class="codeThemeClasses"
    v-html="content"
  ></div>
</template>
