<template>
  <div>
    <NuxtLayout :name="layout">
      <button
        class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
        @click="addRecipe"
      >
        Add Recipe
      </button>
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { authStore } from "../../stores/authStore";
import { definePageMeta } from "#imports";
import { useCustomFetch } from "../../composables/useCustomFetch";
import { useState } from "nuxt/app";
const auth = authStore();
const layout = "dashboard";
const recipe: any = useCustomFetch("recipe");
let user: any = useState();

const fetchUser = async () => {
  const fetchUser = await auth.fetchUser();
  user = fetchUser;
};

definePageMeta({
  middleware: ["auth"],
});

const addRecipe = async () => {};

fetchUser();
</script>
