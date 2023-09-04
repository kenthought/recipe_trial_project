<template>
  <div>
    <NuxtLayout :name="layout">
      <div class="bg-white">
        <div
          class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
          v-if="pending"
        >
          <p>Loading...</p>
        </div>
        <div
          class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
          v-else-if="error"
        >
          <p>{{ error }}</p>
        </div>
        <div
          class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
          v-else-if="recipe.length != 0"
        >
          <div class="group relative" v-for="item in recipe">
            <div
              class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80"
            >
              <img
                src="https://picsum.photos/200/300"
                :alt="item.recipe"
                class="h-full w-full object-cover object-center lg:h-full lg:w-full"
              />
            </div>
            <div class="mt-4 flex justify-between">
              <div>
                <h3 class="text-sm text-gray-700">
                  <NuxtLink :to="'dashboard/recipe/' + item.id">
                    <span aria-hidden="true" class="absolute inset-0"></span>
                    {{ item.recipe }}
                  </NuxtLink>
                </h3>
                <p class="mt-1 text-sm text-gray-500">
                  By: {{ item.user.first_name }}
                </p>
              </div>
              <!-- <p class="text-sm font-medium text-gray-900">$35</p> -->
            </div>
          </div>
        </div>
        <div
          class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
          v-else
        >
          <p>No recipes yet</p>
        </div>
      </div>
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { authStore } from "~/stores/authStore";
import { definePageMeta } from "#imports";

const auth = authStore();
await auth.fetchUser();
const layout = "dashboard";
const {
  data: recipe,
  pending,
  refresh,
  error,
}: any = useCustomFetch("recipe/");

definePageMeta({
  middleware: ["auth"],
});
</script>
