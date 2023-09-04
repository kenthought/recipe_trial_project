<template>
  <NuxtLayout :name="layout">
    <div class="bg-white">
      <div>
        <div class="inline-flex rounded-md shadow-sm mb-3" role="group">
          <button
            type="button"
            class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-l-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
            @click="
              addUser = false;
              usersTable = true;
            "
          >
            <svg
              class="w-[14px] h-[14px] text-gray-800 dark:text-white mr-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z"
              />
            </svg>
            Users
          </button>
          <button
            type="button"
            class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-r-md hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
            @click="
              addUser = true;
              usersTable = false;
              editData = {};
            "
          >
            <svg
              class="w-[14px] h-[14px] text-gray-800 dark:text-white mr-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 20 18"
            >
              <path
                d="M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z"
              />
            </svg>
            Add users
          </button>
        </div>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
          <UsersTable
            v-if="usersTable"
            showUsersTable:showUsersTable
            showAddUser:showAddUser
          />
          <AddUser v-if="addUser" />
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>
<script setup lang="ts">
import { authStore } from "~/stores/authStore";
import { definePageMeta } from "#imports";
definePageMeta({
  middleware: ["auth", "admin"],
  layout: false,
});
const usersTable = useUsersTable();
const addUser = useAddUser();
const isEditing = useIsEditing();
const editData = useEditData();
const layout = "admin";
</script>
