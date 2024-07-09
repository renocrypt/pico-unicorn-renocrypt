<script setup lang="ts">
import { Button } from "@/components/ui/button";
import { Paintbrush, PaintBucket } from "lucide-vue-next";
import { watch } from "vue";

const props = defineProps<{
  isDarkTheme: boolean;
}>();

const emit = defineEmits<{
  (e: "toggle"): void;
}>();

// Synchronize with NavHeader
watch(
  () => props.isDarkTheme,
  (newValue) => {
    document.documentElement.classList.toggle("dark", newValue);
  }
);
</script>

<template>
  <Button @click="emit('toggle')" variant="outline" size="icon">
    <Paintbrush v-if="isDarkTheme" class="h-[1.2rem] w-[1.2rem]" />
    <PaintBucket v-else class="h-[1.2rem] w-[1.2rem]" />
    <span class="sr-only">Toggle theme</span>
  </Button>
</template>
```
