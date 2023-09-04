<template>
  <NuxtLayout :name="layout">
    <div class="bg-white">
      <div class="pt-6" v-if="pending">
        <p>Loading...</p>
      </div>
      <div class="pt-6" v-else-if="error">
        <p>{{ error }}</p>
      </div>
      <div class="pt-6" v-else>
        <nav aria-label="Breadcrumb" v-if="data.user.id == user.id">
          <ol
            role="list"
            class="mx-auto flex max-w-2xl items-center space-x-2 px-4 sm:px-6 lg:max-w-7xl lg:px-8"
          >
            <li>
              <button
                class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
                @click="addRecipeModal = true"
              >
                Edit
              </button>
            </li>

            <li class="text-sm">
              <button
                class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
                @click="deleteRecipeModal = true"
              >
                Delete
              </button>
            </li>
          </ol>
        </nav>

        <!-- Recipe info -->
        <div
          class="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16"
        >
          <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
            <h1
              class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl"
            >
              {{ data.recipe }}
            </h1>
          </div>

          <div class="mt-4 lg:row-span-3 lg:mt-0">
            <div
              class="aspect-h-5 aspect-w-4 lg:aspect-h-4 lg:aspect-w-3 sm:overflow-hidden sm:rounded-lg"
            >
              <img
                src="https://picsum.photos/200/300"
                alt="Model wearing plain white basic tee."
                class="h-full w-full object-cover object-center"
              />
            </div>
          </div>

          <div
            class="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pb-16 lg:pr-8 lg:pt-6"
          >
            <div class="mt-10">
              <h3 class="text-sm font-medium text-gray-900">Ingredients</h3>

              <div class="mt-4">
                <p class="text-sm text-gray-600">
                  {{ data.ingredients }}
                </p>
              </div>
            </div>

            <div class="mt-10">
              <h2 class="text-sm font-medium text-gray-900">Instructions</h2>

              <div class="mt-4 space-y-6">
                <p class="text-sm text-gray-600">
                  {{ data.instructions }}
                </p>
              </div>
            </div>
          </div>
        </div>
        <AddRecipeModal
          v-show="addRecipeModal"
          @close-modal="addRecipeModal = false"
          :refresh="refresh"
          :isEditing="true"
          :editData="JSON.stringify({ ...data })"
        />
        <DeleteRecipeModal
          v-show="deleteRecipeModal"
          @close-modal="deleteRecipeModal = false"
          :data="JSON.stringify({ ...data })"
        />
      </div>
    </div>
  </NuxtLayout>
</template>
<script setup lang="ts">
import { authStore } from "~/stores/authStore";
import { definePageMeta } from "#imports";

const auth = authStore();
const route = useRoute();
const layout = "dashboard";
const addRecipeModal = ref(false);
const deleteRecipeModal = ref(false);
await auth.fetchUser();
const user: any = auth.user;
const { data, error, pending, refresh }: any = useCustomFetch(
  "recipe/" + route.params.id,
  {
    lazy: true,
  }
);
console.log();

definePageMeta({
  middleware: ["auth"],
  layout: false,
});
</script>
