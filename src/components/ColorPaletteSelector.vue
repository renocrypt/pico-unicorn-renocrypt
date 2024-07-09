<script setup lang="ts">
import { ref, computed } from "vue";
import { Check, ChevronsUpDown } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
} from "@/components/ui/command";

const colorPalettes = [
  { name: "Pastel Rainbow", value: "pastel-rainbow" },
  { name: "Ocean Breeze", value: "ocean-breeze" },
  { name: "Spring Bloom", value: "spring-bloom" },
  { name: "Sunset Glow", value: "sunset-glow" },
  { name: "Forest Mist", value: "forest-mist" },
];

const open = ref(false);
const selectedPalette = ref(colorPalettes[0]);
const searchQuery = ref("");

const filteredPalettes = computed(() => {
  return colorPalettes.filter((palette) =>
    palette.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const emit = defineEmits<{
  (e: "select", palette: (typeof colorPalettes)[0]): void;
}>();

const selectPalette = (palette: (typeof colorPalettes)[0]) => {
  selectedPalette.value = palette;
  open.value = false;
  emit("select", palette);
};
</script>

<template>
  <Popover v-model:open="open">
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        role="combobox"
        aria-expanded="open"
        class="w-[200px] justify-between"
      >
        {{ selectedPalette.name }}
        <ChevronsUpDown class="ml-2 h-4 w-4 shrink-0 opacity-50" />
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-[200px] p-0">
      <Command>
        <CommandInput placeholder="Search palette..." v-model="searchQuery" />
        <CommandEmpty>No palette found.</CommandEmpty>
        <CommandGroup>
          <CommandItem
            v-for="palette in filteredPalettes"
            :key="palette.value"
            @select="() => selectPalette(palette)"
          >
            <Check
              :class="[
                'mr-2 h-4 w-4',
                selectedPalette.value === palette.value
                  ? 'opacity-100'
                  : 'opacity-0',
              ]"
            />
            {{ palette.name }}
          </CommandItem>
        </CommandGroup>
      </Command>
    </PopoverContent>
  </Popover>
</template>
