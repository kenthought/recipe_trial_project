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
        <div v-else-if="recipe.length != 0">
          <button
            class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
            @click="
              isEditing = false;
              addRecipeModal = true;
            "
          >
            Add Recipe
          </button>
          <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table
              class="w-full text-sm text-left text-gray-500 dark:text-gray-400"
            >
              <thead
                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
              >
                <tr>
                  <!-- <th scope="col" class="p-4">
                    <div class="flex items-center">
                      <input
                        id="checkbox-all-search"
                        type="checkbox"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                      />
                      <label for="checkbox-all-search" class="sr-only"
                        >checkbox</label
                      >
                    </div>
                  </th> -->
                  <th scope="col" class="px-6 py-3">Recipe</th>
                  <th scope="col" class="px-6 py-3">User</th>
                  <th scope="col" class="px-6 py-3">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
                  v-for="item in recipe"
                >
                  <!-- <td class="w-4 p-4">
                    <div class="flex items-center">
                      <input
                        id="checkbox-table-search-1"
                        type="checkbox"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                      />
                      <label for="checkbox-table-search-1" class="sr-only"
                        >checkbox</label
                      >
                    </div>
                  </td> -->
                  <th
                    scope="row"
                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    {{ item.recipe }}
                  </th>
                  <td class="px-6 py-4">{{ item.user.first_name }}</td>
                  <td class="flex items-center px-6 py-4 space-x-3">
                    <a
                      href="#"
                      class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
                      @click="handleEdit(item)"
                      >Edit</a
                    >
                    <a
                      href="#"
                      class="font-medium text-red-600 dark:text-red-500 hover:underline"
                      @click="handleDelete(item)"
                      >Remove</a
                    >
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Modals -->
          <AddRecipeModal
            v-if="addRecipeModal"
            @close-modal="addRecipeModal = false"
            :refresh="refresh"
            :isEditing="isEditing"
            :editData="JSON.stringify(editData)"
            :redirect="true"
          />
          <DeleteRecipeModal
            v-if="deleteRecipeModal"
            @close-modal="deleteRecipeModal = false"
            :data="JSON.stringify(editData)"
            :redirect="false"
            :refresh="refresh"
          />
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
const layout = "admin";
const {
  data: recipe,
  pending,
  refresh,
  error,
}: any = useCustomFetch("recipe/");
let addRecipeModal = ref(false);
let deleteRecipeModal = ref(false);
let isEditing: boolean = false;
let editData: Object = {};

const handleEdit = (data: Object) => {
  let temp: any = JSON.stringify(data);
  temp = JSON.parse(temp);
  temp.user = temp.user.id;
  editData = temp;
  isEditing = true;
  addRecipeModal = ref(true);
};

const handleDelete = (data: Object) => {
  let temp: any = JSON.stringify(data);
  temp = JSON.parse(temp);
  temp.user = temp.user.id;
  editData = temp;
  deleteRecipeModal = ref(true);
};

definePageMeta({
  middleware: ["auth", "admin"],
  layout: false,
});
</script>
