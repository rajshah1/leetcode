class Solution {
    public String tree2str(TreeNode root) {
        if(root == null)
            return "";
        if(root.left == null && root.right == null) 
            return String.valueOf(root.val);
        else if(root.left != null && root.right != null)
            return root.val+"("+tree2str(root.left)+")"+"("+tree2str(root.right)+")";
        else if(root.left != null && root.right == null)
            return root.val + "("+tree2str(root.left)+")";
        else 
            return root.val + "()" +"("+tree2str(root.right)+")";
    }
}
