<script setup lang="ts">
import { Skeleton } from "@/components/ui/skeleton";

defineProps<{
  title: string;
  date: string;
  isLoading: boolean;
}>();
</script>

<template>
  <div class="mb-8">
    <Skeleton v-if="isLoading" class="w-2/3 h-10 mb-4" />
    <h1 v-else class="text-3xl font-bold mb-2">{{ title }}</h1>
    <Skeleton v-if="isLoading" class="w-1/3 h-6" />
    <p v-else class="text-sm opacity-70">{{ date }}</p>
  </div>
</template>
