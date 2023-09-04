<template>
  <NuxtLayout :name="layout">
    <div>users</div>
  </NuxtLayout>
</template>
<script setup lang="ts">
import { definePageMeta } from "#imports";
const layout = "admin";

definePageMeta({
  middleware: ["auth"],
  layout: false,
});
</script>
