// Admin states
export const useUsersTable = () => useState<boolean>("usersTable", () => true);
export const useAddUser = () => useState<boolean>("addUser", () => false);
export const useDeleteUser = () => useState<boolean>("deleteUser", () => false);
export const useIsEditing = () => useState<boolean>("isEditing", () => false);
export const useEditData = () => useState("editData", () => {});